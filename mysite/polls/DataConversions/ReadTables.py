import pandas as pd
import pyodbc
import numpy as np

import warnings
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Maike\Desktop\CompleetSterSchema.accdb;')

def ComposeEmployeeTable():
    '''Composes the Employee Table according to the ETL.'''
    Employee = pd.read_sql("SELECT Emp_id, dept_id, bene_health_ins, bene_day_care, emp_fname, emp_lname FROM employee", conn)
    Department =  pd.read_sql("SELECT dept_name, dept_id, dept_head_id FROM department", conn)
    res = pd.merge(Employee, Department, on = 'dept_id', how='left')
    return res

def ComposeProductTable():
    '''Composes the Employee Table according to the ETL.'''
    Product = pd.read_sql("SELECT id, name, description FROM product", conn)
    # print(Product)
    
    return Product

def ComposedateTable():
    '''Composes the Employee Table according to the ETL.'''
    date = pd.read_sql("SELECT order_date FROM sales_order", conn)
    date['order_date'] = pd.Series(np.unique(date['order_date']))
    date['order_date'] = pd.to_datetime(date['order_date'])
    date = date.dropna()
    date['month'] = date['order_date'].dt.month
    date['year'] = date['order_date'].dt.year

    print(date)
    # return date




if __name__ ==  "__main__":
    # df = ComposedateTable()
    # print(ComposeProductTable())
    df = ComposeEmployeeTable()
    # df = cleanEmpl(df)
    print(df)
    # parseDate()