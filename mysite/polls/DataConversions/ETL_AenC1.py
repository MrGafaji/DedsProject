import pandas as pd
import pyodbc
import numpy as np
from SupabaseInterface import SupabaseInterface as db, genID


base = db()

### A&C 1

def ComposeProductTable():
    Product = base.GetFullTable('product2')
    '''Composes the Product Table according to the ETL.'''
    Product = Product[['id', 'name', 'description']]    
    return Product

def ComposedateTable():
    '''Composes the Date Table according to the ETL.'''
    sales_order = base.GetFullTable('SalesOrders')
    # print(sales_order.info())
    date = sales_order[['order_date']]
    date['order_date'] = pd.Series(np.unique(date['order_date']))
    date['order_date'] = pd.to_datetime(date['order_date'])
    print(date.info())
    # date = date.dropna()
    # date['month'] = date['order_date'].dt.month
    # date['year'] = date['order_date'].dt.year

    # print(date)
    return date

def ComposeSalesOrder():
    sales_order_item = base.GetFullTable('salesOrderItem')
    product = base.GetFullTable('product2')
    sales_order = base.GetFullTable('SalesOrders')
    Sales_order_item =  sales_order_item[['id', 'prod_id', 'quantity']]
    Product = product[['id', 'unit_price']]
    Sales_order = sales_order[['id', 'order_date', 'region']]
    res = pd.merge(Sales_order_item, Product, how='left', left_on='prod_id', right_on='id')
    res = pd.merge(res, Sales_order, how='left', left_on='id_x', right_on='id')
    res.drop(['id'], axis=1, inplace=True)
    res.rename({'id_x': 'sales_order_id', 'prod_id': 'sales_order_prod_id', 'quantity': 'sales_order_prod_quantity', 'id_y':'Product_id', 'unit_price':'sales_order_unit_price', 'region':'Region_region', 'order_date': 'Date_date'}, axis=1, inplace=True)
    res = res[['sales_order_id', 'sales_order_prod_id', 'sales_order_prod_quantity', 'sales_order_unit_price','Product_id', 'Region_region', 'Date_date']]
    return res

if __name__ ==  "__main__":
    df = ComposedateTable()
    # df = ComposeProductTable()
    # df = ComposeSalesOrder()
    # df = cleanEmpl(df)
    # print(df)
    # parseDate()