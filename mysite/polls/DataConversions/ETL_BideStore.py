import pandas as pd
import pyodbc
import numpy as np
from SupabaseInterface import SupabaseInterface as db, genID

base = db()
sales = base.GetFullTable('Sales')

### BikeStore
def ComposeSales():
    Sales = sales.reset_index()
    Sales = Sales.rename(columns={"index":"Sales_ID"})
    Product = ComposeProductTable()
    Country = ComposeCountry()
    Customer = ComposeCustomerTable()
    Sales = pd.merge(Sales, Product, on=['Product', 'Product_Category', 'Sub_Category'], how='left')
    Sales = pd.merge(Sales, Country, on=['Country', 'State'], how='left')
    Sales = Sales.drop(['Product', 'Product_Category', 'Sub_Category', 'Country', 'State', 'Day', 'Month', 'Year', 'Unit_Cost', 'Profit'], axis=1)
    Sales = pd.merge(Sales, Customer, on=['Customer_Age', 'Age_Group', 'Customer_Gender'], how='left')
    Sales = Sales.drop(['Customer_Age', 'Age_Group', 'Customer_Gender'], axis = 1)
    
    return Sales

def ComposeProductTable():
    '''Composes the Employee Table according to the ETL.'''
    Product = sales[['Product', 'Product_Category', 'Sub_Category']]
    Product = Product.drop_duplicates()
    Product = Product.reset_index()
    Product = Product.drop(columns={"index"})
    Product = Product.reset_index()
    Product = Product.rename(columns={"index":"Product_ID"})

    return Product

def ComposedateTable():
    '''Composes the Employee Table according to the ETL.'''
    date = sales[['Date']]
    date['order_date'] = pd.Series(np.unique(date['Date']))
    date['order_date'] = pd.to_datetime(date['Date'], format='%d-%m-%Y %H:%M:%S')
    date = date.dropna()
    date['month'] = date['order_date'].dt.month
    date['year'] = date['order_date'].dt.year

    return date

def ComposeCustomerTable():
    Customer = sales[['Customer_Age', 'Age_Group', 'Customer_Gender']]
    Customer = Customer.reset_index()
    Customer = Customer.rename(columns={"index":"C_ID"})

    return Customer

def ComposeCountry():
    Country = sales[['Country', 'State']]
    Country = Country.drop_duplicates()
    Country = Country.reset_index()
    Country = Country.rename(columns={"index":"Country_ID"})

    return Country
    
if __name__ ==  "__main__":
    #df = ComposeProductTable()
    #df = ComposedateTable()
    #df = ComposeCustomerTable()
    #df = ComposeCountry()
    df = ComposeSales()
    print(df)