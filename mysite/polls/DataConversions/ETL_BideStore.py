import pandas as pd
import pyodbc
import numpy as np
from DBConnectie import DBConn

### BikeStore
def GetSalesTable():
    Sales = DBConn.toDf(DBConn.salesSUP)
    print(Sales.columns)
    Product = Sales[['Product', 'Product_Category', 'Sub_Category']]
    Customer = Sales[[]]



    return Product


# def ComposeProductTable():
#     '''Composes the Employee Table according to the ETL.'''
#     Product = pd.read_sql("SELECT id, name, description FROM product", conn)
#     # print(Product)
    
#     return Product

# def ComposedateTable():
#     '''Composes the Employee Table according to the ETL.'''
#     date = pd.read_sql("SELECT order_date FROM sales_order", conn)
#     date['order_date'] = pd.Series(np.unique(date['order_date']))
#     date['order_date'] = pd.to_datetime(date['order_date'])
#     date = date.dropna()
#     date['month'] = date['order_date'].dt.month
#     date['year'] = date['order_date'].dt.year

# #     # print(date)
# #     return date

# # def ComposeSalesOrder():
# #     Sales_order_item =  pd.read_sql("SELECT id, prod_id, quantity FROM sales_order_item", conn)
# #     Product =  pd.read_sql("SELECT id , unit_price FROM product", conn)
# #     Sales_order =  pd.read_sql("SELECT id, order_date, cust_id, sales_rep FROM sales_order", conn)
# #     Employee = pd.read_sql("SELECT emp_id, emp_fname, salary FROM employee", conn)
# #     bonus = pd.read_sql("SELECT * FROM bonus", conn)
# #     res = pd.merge(Sales_order_item, Product, how='left', left_on='prod_id', right_on='id')
# #     res = pd.merge(res, Sales_order, how='left', left_on='id_x', right_on='id')
# #     res = pd.merge(res, Employee, how='left', left_on='sales_rep', right_on='emp_id')
# #     res = pd.merge(res, bonus, how='left', left_on='emp_id', right_on='emp_id')
# #     # res.drop(['id'], axis=1, inplace=True)
# #     res.rename({'id_x': 'sales_order_id','id':'Product_id', 'prod_id': 'sales_order_prod_id', 'quantity': 'sales_order_prod_quantity', 'unit_price':'sales_order_unit_price', 'salary':'sales_order_employee_salary', 'bonus_amount': 'sales_order_bonus_bonus_amount', 'emp_id': 'Employee_id', 'order_date':'Date_date'}, axis=1, inplace=True)
# #     res = res[['sales_order_id', 'sales_order_prod_id', 'sales_order_prod_quantity', 'sales_order_unit_price', 'sales_order_employee_salary', 'sales_order_bonus_bonus_amount', 'Product_id', 'Employee_id', 'Date_date']]
# #     # print(res.columns)
# #     return res




if __name__ ==  "__main__":
    df = GetSalesTable()
    print(df)