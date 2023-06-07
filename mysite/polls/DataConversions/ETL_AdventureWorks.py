import pandas as pd
import pyodbc
import numpy as np
from SupabaseInterface import SupabaseInterface as db, genID

base = db()


### AdventureWorks
def ComposeLeverancierTable(Leveranciers):
    Leveranciers = Leveranciers[['BusinessEntityID', 'Name']]
    Leveranciers['BusinessEntityID'] = Leveranciers['BusinessEntityID'].astype('int64')

    return Leveranciers

def ComposeProductTable(Product):
    '''Composes the Product Table according to the ETL.'''
    Product = Product[['ProductID','Name']]
    Product = Product.rename(columns={"ProductID": 'id', 'Name': 'name'})
    
    return Product

def ComposedateTable():
    '''Composes the Date Table according to the ETL.'''
    sales_order = base.GetFullTable('SalesOrderHeader')
    date = sales_order[['OrderDate']]
    date['OrderDate'] = pd.Series(np.unique(date['OrderDate']))
    date['OrderDate'] = pd.to_datetime(date['OrderDate'], format="%d-%m-%Y %H:%M:%S")
    print(date.info())
    date = date.dropna()
    date['month'] = date['OrderDate'].dt.month
    date['year'] = date['OrderDate'].dt.year

    # print(date)
    return date


def ComposeSoldProductProductTable(SalesOrderHeader, SalesOrderDetail, ProductVendor):
    SalesOrderDetail = SalesOrderDetail
    SalesOrderHeader = SalesOrderHeader
    ProductVendor = ProductVendor

    return SalesOrderHeader
    



if __name__ ==  "__main__":
    # df = ComposeSoldProductProductTable()
    #ComposeSoldProductProductTable()
    df = ComposedateTable()
    # print(5)
    # print(df)
    print(6)
    # print(df.info())