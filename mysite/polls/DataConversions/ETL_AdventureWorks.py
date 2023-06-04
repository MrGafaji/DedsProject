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
    



if __name__ ==  "__main__":
    df = ComposeSoldProductProductTable()
    print(df)
    print(df.info())