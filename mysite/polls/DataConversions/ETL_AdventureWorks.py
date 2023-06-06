import pandas as pd
import pyodbc
import numpy as np
from DBConnectie import DBConn

Leveranciers = DBConn.toDf(DBConn.vendorSUP)
Product = DBConn.toDf(DBConn.productionProductSUP)
SalesOrderHeader = DBConn.toDf(DBConn.salesOrderHeaderSUP)
SalesOrderDetail = DBConn.toDf(DBConn.salesOrderDetailSUP)
ProductVendor = DBConn.toDf(DBConn.productVendorSUP)

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

def ComposedateTable(SalesOrderHeader):
    '''Composes the Date Table according to the ETL.'''
    date = SalesOrderHeader[['OrderDate']]
    date['OrderDate'] = pd.Series(pd.unique(date['OrderDate']))
    date['OrderDate'] = pd.to_datetime(date['OrderDate'])
    date = date.dropna()
    date['month'] = date['OrderDate'].dt.month
    date['year'] = date['OrderDate'].dt.year

# #     # print(date)
    return date


def ComposeSoldProductProductTable(SalesOrderHeader, SalesOrderDetail, ProductVendor):
    SalesOrderDetail = SalesOrderDetail
    SalesOrderHeader = SalesOrderHeader
    ProductVendor = ProductVendor

    return SalesOrderHeader
    



if __name__ ==  "__main__":
    df = ComposeSoldProductProductTable(SalesOrderHeader)#ComposeSoldProductProductTable()
    print(df)
    print(df.info())