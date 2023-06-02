import pandas as pd
import pyodbc
import numpy as np

import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Maike\Desktop\CompleetSterSchema.accdb;')

### AdventureWorks
def ComposeLeverancierTable():
    Leveranciers = pd.read_sql("select BusinessEntityID, Name from dbo_Purchasing_Vendor", conn)
    Leveranciers['BusinessEntityID'] = Leveranciers['BusinessEntityID'].astype('int64')

    return Leveranciers

def ComposeProductTable():
    '''Composes the Product Table according to the ETL.'''
    Product = pd.read_sql("SELECT ProductID, Name FROM dbo_Production_Product", conn)
    # print(Product)
    
    return Product

def ComposedateTable():
    '''Composes the Date Table according to the ETL.'''
    date = pd.read_sql("SELECT OrderDate FROM dbo_Sales_SalesOrderHeader", conn)
    date['OrderDate'] = pd.Series(pd.unique(date['OrderDate']))
    date['OrderDate'] = pd.to_datetime(date['OrderDate'])
    date = date.dropna()
    date['month'] = date['OrderDate'].dt.month
    date['year'] = date['OrderDate'].dt.year

# #     # print(date)
    return date


def ComposeSoldProductProductTable():
    SalesOrderDetail = pd.read_sql("select SalesOrderDetailID, SalesOrderID, ProductID, ProductID  from dbo_Sales_SalesOrderDetail", conn)
    ProductVendor = pd.read_sql("select BusinessEntityID from dbo_Purchasing_ProductVendor", conn)
    SalesOrderHeader = pd.read_sql("select * from dbo_Sales_SalesOrderHeader", conn)

    return SalesOrderHeader
    


# def ComposeSalesOrder():
#     Sales_order_item =  pd.read_sql("SELECT id, prod_id, quantity FROM sales_order_item", conn)
#     Product =  pd.read_sql("SELECT id , unit_price FROM product", conn)
#     Sales_order =  pd.read_sql("SELECT id, order_date, cust_id, sales_rep FROM sales_order", conn)
#     Employee = pd.read_sql("SELECT emp_id, emp_fname, salary FROM employee", conn)
#     bonus = pd.read_sql("SELECT * FROM bonus", conn)
#     res = pd.merge(Sales_order_item, Product, how='left', left_on='prod_id', right_on='id')
#     res = pd.merge(res, Sales_order, how='left', left_on='id_x', right_on='id')
#     res = pd.merge(res, Employee, how='left', left_on='sales_rep', right_on='emp_id')
#     res = pd.merge(res, bonus, how='left', left_on='emp_id', right_on='emp_id')
#     # res.drop(['id'], axis=1, inplace=True)
#     res.rename({'id_x': 'sales_order_id','id':'Product_id', 'prod_id': 'sales_order_prod_id', 'quantity': 'sales_order_prod_quantity', 'unit_price':'sales_order_unit_price', 'salary':'sales_order_employee_salary', 'bonus_amount': 'sales_order_bonus_bonus_amount', 'emp_id': 'Employee_id', 'order_date':'Date_date'}, axis=1, inplace=True)
#     res = res[['sales_order_id', 'sales_order_prod_id', 'sales_order_prod_quantity', 'sales_order_unit_price', 'sales_order_employee_salary', 'sales_order_bonus_bonus_amount', 'Product_id', 'Employee_id', 'Date_date']]
#     # print(res.columns)
#     return res




if __name__ ==  "__main__":
    df = ComposeSoldProductProductTable()
    print(df)
    print(df.info())