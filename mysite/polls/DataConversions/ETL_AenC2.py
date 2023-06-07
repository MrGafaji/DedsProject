import pandas as pd
import pyodbc
import numpy as np
from DBConnectie import DBConn

employee = DBConn.toDf(DBConn.employeeSUP)
department = DBConn.toDf(DBConn.departmentSUP)
Product = DBConn.toDf(DBConn.productSUP)
bonus = DBConn.toDf(DBConn.bonusSUP)
sales_order = DBConn.toDf(DBConn.sales_orderSUP)
sales_order_item = DBConn.toDf(DBConn.sales_order_itemSUP)

### A&C 2
def ComposeEmployeeTable(department, employee):
    '''Composes the Employee Table according to the ETL.'''
    Employee = employee[['emp_id', 'dept_id', 'bene_health_ins', 'bene_day_care', 'emp_fname', 'emp_lname']]
    Department = department[['dept_name', 'dept_id', 'dept_head_id']]
    res = pd.merge(Employee, Department, on = 'dept_id', how='left')
    return res

def ComposeProductTable(product):
    '''Composes the Employee Table according to the ETL.'''
    Product = product[['id', 'name', 'description']]
    
    return Product

def ComposedateTable(sales_order):
    '''Composes the Employee Table according to the ETL.'''
    date = sales_order[['order_date']] 
    date['order_date'] = pd.Series(np.unique(date['order_date']))
    date['order_date'] = pd.to_datetime(date['order_date'])
    date = date.dropna()
    date['month'] = date['order_date'].dt.month
    date['year'] = date['order_date'].dt.year

    # print(date)
    return date

def ComposeSalesOrder(sales_order_item, Product, sales_order, employee, bonus):
    Sales_order_item = sales_order_item[['id', 'prod_id', 'quantity']] 
    Product = Product[['id' , 'unit_price']] 
    Sales_order = sales_order[['id', 'order_date', 'cust_id', 'sales_rep']] 
    Employee = employee[['emp_id', 'emp_fname', 'salary']]
    res = pd.merge(Sales_order_item, Product, how='left', left_on='prod_id', right_on='id')
    res = pd.merge(res, Sales_order, how='left', left_on='id_x', right_on='id')
    res = pd.merge(res, Employee, how='left', left_on='sales_rep', right_on='emp_id')
    res = pd.merge(res, bonus, how='left', left_on='emp_id', right_on='emp_id')
    # res.drop(['id'], axis=1, inplace=True)
    res.rename({'id_x': 'sales_order_id','id':'Product_id', 'prod_id': 'sales_order_prod_id', 'quantity': 'sales_order_prod_quantity', 'unit_price':'sales_order_unit_price', 'salary':'sales_order_employee_salary', 'bonus_amount': 'sales_order_bonus_bonus_amount', 'emp_id': 'Employee_id', 'order_date':'Date_date'}, axis=1, inplace=True)
    res = res[['sales_order_id', 'sales_order_prod_id', 'sales_order_prod_quantity', 'sales_order_unit_price', 'sales_order_employee_salary', 'sales_order_bonus_bonus_amount', 'Product_id', 'Employee_id', 'Date_date']]
    # print(res.columns)
    return res




if __name__ ==  "__main__":
    #df = ComposedateTable(sales_order)
    # print(ComposeProductTable())
    #df = ComposeEmployeeTable(department, employee)
    df = ComposeSalesOrder(sales_order_item, Product, sales_order, employee, bonus)
    # df = cleanEmpl(df)
    print(df)
    # parseDate()