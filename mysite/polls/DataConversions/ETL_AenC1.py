import pandas as pd
import pyodbc
import numpy as np
from DBConnectie import DBConn

Product = DBConn.toDf(DBConn.productSUP)
sales_order = DBConn.toDf(DBConn.sales_orderSUP)
sales_order_item = DBConn.toDf(DBConn.sales_order_itemSUP)


### A&C 1

def ComposeProductTable(Product):
    '''Composes the Product Table according to the ETL.'''
    Product = Product[['id', 'name', 'description']]    
    return Product

def ComposedateTable(sales_order):
    '''Composes the Date Table according to the ETL.'''
    date = sales_order[['order_date']]
    date['order_date'] = pd.Series(np.unique(date['order_date']))
    date['order_date'] = pd.to_datetime(date['order_date'])
    date = date.dropna()
    date['month'] = date['order_date'].dt.month
    date['year'] = date['order_date'].dt.year

    # print(date)
    return date

def ComposeSalesOrder(sales_order_item, product, sales_order):
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
    #df = ComposedateTable(sales_order)
    #df = ComposeProductTable(Product)
    #df = ComposeSalesOrder(sales_order_item, Product, sales_order)
    # df = cleanEmpl(df)
    print(df)
    # parseDate()