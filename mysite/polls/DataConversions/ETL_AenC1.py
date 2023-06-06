import pandas as pd
import pyodbc
import numpy as np

import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Maike\Desktop\CompleetSterSchema.accdb;')

### A&C 1

def ComposeProductTable():
    '''Composes the Product Table according to the ETL.'''
    Product = pd.read_sql("SELECT id, name, description, color, Category FROM product", conn)    
    Product = Product.rename(columns={'Category': 'category'})
    return Product

def ComposedateTable():
    '''Composes the Date Table according to the ETL.'''
    date = pd.read_sql("SELECT order_date FROM sales_order", conn)
    date['order_date'] = pd.Series(np.unique(date['order_date']))
    date['order_date'] = pd.to_datetime(date['order_date'])
    date = date.dropna()
    date['month'] = date['order_date'].dt.month
    date['year'] = date['order_date'].dt.year

    # print(date)
    return date

def ComposeSalesOrder():
    Sales_order_item =  pd.read_sql("SELECT id, prod_id, quantity FROM sales_order_item", conn)
    Product =  pd.read_sql("SELECT id , unit_price FROM product", conn)
    Sales_order =  pd.read_sql("SELECT id, order_date, region FROM sales_order", conn)
    res = pd.merge(Sales_order_item, Product, how='left', left_on='prod_id', right_on='id')
    res = pd.merge(res, Sales_order, how='left', left_on='id_x', right_on='id')
    res.drop(['id'], axis=1, inplace=True)
    res.rename({'id_x': 'sales_order_id', 'prod_id': 'sales_order_prod_id', 'quantity': 'sales_order_prod_quantity', 'id_y':'Product_id', 'unit_price':'sales_order_unit_price', 'region':'Region_region', 'order_date': 'Date_date'}, axis=1, inplace=True)
    res = res[['sales_order_id', 'sales_order_prod_id', 'sales_order_prod_quantity', 'sales_order_unit_price','Product_id', 'Region_region', 'Date_date']]
    return res

if __name__ ==  "__main__":
    # df = ComposedateTable()
    # df = ComposeProductTable()
    # df = ComposeEmployeeTable()
    df = ComposeSalesOrder()
    # df = cleanEmpl(df)
    print(df)
    # parseDate()