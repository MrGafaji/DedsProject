import pandas as pd
import pyodbc
import numpy as np

import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
sales_conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Maike\Documents\Projects\DedsProj\DedsProject\mysite\Data\FullDB1.accdb;')

def getProductTable():
    # PRODUCT_NUMBER, PRODUCT_TYPE_CODE 
    product = pd.read_sql("SELECT FirstName, LastName  FROM dbo_Employee", sales_conn)


    print(product)


if __name__ ==  "__main__":
    getProductTable()