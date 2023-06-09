from DataConversions.SupabaseInterface import SupabaseInterface as db, genID

import pandas as pd
import numpy as np
import datetime as dt



    # VerkochtProduct = TODO
def ETL_Fact():
    base = db()
    idgen = genID()

    ### AenC
    orderItem1 = base.GetFullTable('salesOrderItem')
    order1 = base.GetFullTable('SalesOrders')
    product1 = base.GetFullTable('product2')
    sales1 = pd.merge(orderItem1, order1, on='id', how='left')
    sales1 = pd.merge(sales1, product1, left_on='prod_id', right_on='id', how='left', suffixes=('', '_prod'))
    ### AdventureWorks
    orderItem2 = base.GetFullTable('SalesOrderDetail')
    order2 = base.GetFullTable('SalesOrderHeader')
    sales2 = pd.merge(orderItem2, order2, on='SalesOrderID', how='left')
    productVendor = base.GetFullTable('ProductVendor')
    sales2 = pd.merge(sales2, productVendor, on='ProductID', how='left', suffixes=("","_pv"))

    # print(sales1)
    # print(sales2)
    frame1 = pd.DataFrame({
        'order_id'      : sales1['id'], 
        'orderline_id'  : sales1['line_id'], 
        'quantity'      : sales1['quantity'], 
        'productId'     : sales1['prod_id'], 
        'UnitPrice'     : sales1['unit_price'], 
        'Date'          : sales1['order_date'],
        'employee_id'   : sales1['sales_rep'],
        'TerritoryID'   : sales1['region'],
        # 'customer_Id'   : sales1['cust_id'],
        'Vendor_Id'     : None
    })
    # print(sales1.iloc[0])
    frame2 = pd.DataFrame({
        'order_id'      : sales2['SalesOrderID'], 
        'orderline_id'  : sales2['SalesOrderDetailID'], 
        'quantity'      : sales2['OrderQty'], 
        'productId'     : sales2['ProductID'], 
        'UnitPrice'     : sales2['UnitPrice'], 
        'Date'          : sales2['OrderDate'],
        'employee_id'   : sales2['SalesPersonID'],
        'TerritoryID'   : sales2['TerritoryID'],
        # 'customer_Id'   : sales2['CustomerID'],
        'Vendor_Id'     : sales2['BusinessEntityID'],
    })
    # print(frame2)
    def dateReformatFrame2(x):
        if type(x) == float:
            # print('m')
            return None
        # print(f'{x = }, type: {type(x)}')
        x = x.split(' ')[0]
        d, m, y = x.split('-')
        # print(f'{d = }, {m = }, {y = }')

        date = str(dt.date(int(y), int(m), int(d)))
        # print("dddddddddd" , date)
        return date

    frame2['UnitPrice'] = frame2['UnitPrice'].apply(lambda s: s.replace(',', '.'))
    ###### frame2['Date'] = frame2['Date'].apply(dateReformatFrame2)
    

    # combined = pd.concat([frame1], ignore_index=True)
    combined = pd.concat([frame1, frame2], ignore_index=True)
    
    def vendorize(x):
        try:
            if x != x: return None
            if type(x) == str:
                x = float(x)
                print(f'{int(x) = }')
            return int(x)
        except:
            return None
        
    
        
    

    combined['Vendor_Id'] = combined['Vendor_Id'].apply(vendorize)
    # print(combined)
    

    combined = combined.astype({
        'UnitPrice' : float,
        'productId' : str,
    })
    # print(combined)
    # print(combined.info())

    for _, row in combined.iterrows():
        rowDict = row.to_dict()
        # print(rowDict)

        correspondingProduct = base.GetFirstEntryWhere('F_Product', {"id":rowDict['productId']})
        ProdSID = None if not correspondingProduct else correspondingProduct['s_id']
        if type(rowDict['employee_id']) is not float:
            # print(f'{type(rowDict["employee_id"]) = }')
            try:
                bonusCorr_emp =  base.GetFirstEntryWhere('Bonus', {"emp_id":rowDict['employee_id']})
            except:
                bonusCorr_emp = None
        else:
            bonusCorr_emp = None
        BonusAm = None if not bonusCorr_emp else bonusCorr_emp['bonus_amount']

        if len(str(rowDict['TerritoryID']))>3:
            correspState =  base.GetFirstEntryWhere('F_State', {"state":rowDict['TerritoryID']})
            stateId = None if not correspState else correspState['s_id']
        else:
            stateId = rowDict['TerritoryID']


        newRow = {
            's_id'      : idgen.id(),
            'order_id'  : rowDict.get('order_id'),
            'orderline_id'  : rowDict.get('orderline_id'),
            'quantity'  : str(rowDict.get('quantity')),
            'unit_price'  : float(rowDict.get('UnitPrice')),
            'bonus_amount'  : BonusAm,
            # 'unit_cost'  : None,
            'product_s_id'  : ProdSID,
            'employee_id'  : rowDict.get('employee_id'),
            'Date'      : rowDict.get('Date'),
            'Region'  : stateId,
            'Vendor_Id'  : rowDict.get('Vendor_Id'),
            # 'customer_Id'  : rowDict.get('customer_Id'),
            'productId'  : rowDict.get('order_id'),
        }
        for k,v in newRow.items():
            if v != v:
                newRow[k] = None
        # if newRow['Vendor_Id'] == newRow['Vendor_Id']:
        #     newRow['Vendor_Id'] = int(newRow['Vendor_Id'])

        print(newRow)
        # print(f'{type(newRow["Vendor_Id"]) = }')
        if type(newRow["Vendor_Id"]) == float:
            newRow['Vendor_Id'] = int(newRow['Vendor_Id'])
        
        base.AddIfNotAlreadyInDBForFactTable('F_Order_Fact', newRow)

if __name__ == '__main__':
    ETL_Fact()