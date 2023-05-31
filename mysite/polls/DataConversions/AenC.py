import pandas as pd
import pyodbc
import os
from django.http import JsonResponse
from supabase import create_client, Client
from pandas import json_normalize
import json

url: str = 'https://cglhcfmkwabxrvlfuqwb.supabase.co/'
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNnbGhjZm1rd2FieHJ2bGZ1cXdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQxNDk2MzUsImV4cCI6MTk5OTcyNTYzNX0.h-qRysp76hKecbDCjdLaZP03wOaAQ_sl-6_vQ1odb7M"
supabase: Client = create_client(url, key)
data = supabase.auth.sign_in_with_password({"email": "outdoorfusion@gmail.com", "password": "Admin123"})


sales_order_itemSUP = supabase.table('salesOrderItem').select('*').execute().json()
sales_orderSUP = supabase.table('SalesOrders').select('*').execute().json()
productSUP = supabase.table('product2').select('*').execute().json()
employeeSUP = supabase.table('Employee').select('*').execute().json()
departmentSUP = supabase.table('Department').select('*').execute().json()


def toDf(tabel):
    d = json.loads(tabel)
    df = json_normalize(d, 'data')
    return df

sales_order_item = toDf(sales_order_itemSUP)
sales_order = toDf(sales_orderSUP)
product = toDf(productSUP)
employee = toDf(employeeSUP)
department = toDf(departmentSUP)

merged_data = pd.merge(sales_order_item, product, left_on='prod_id', right_on='id')
merged_data = pd.merge(merged_data, sales_order, left_on='id_x', right_on='id')
merged_data['unit_price'] = merged_data['unit_price'].astype(float)
merged_data['order_date'] = pd.to_datetime(merged_data['order_date'])

merged_data2 = pd.merge(employee, department, left_on='dept_id', right_on='dept_id')
merged_data2['salary'] = merged_data2['salary'].astype(float)


def get_sales_amount_per_region(request):
    sales_amount_per_region = merged_data.groupby('region')['unit_price'].sum().reset_index()
    sales_amount_per_region.rename(columns={'unit_price': 'total_sales_amount'}, inplace=True)

    result = {
        'sales_amount_per_region': sales_amount_per_region.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_sales_per_region(request):

    sales_per_region = merged_data.groupby('region')['id'].count().reset_index()
    sales_per_region.rename(columns={'id': 'total_product_sales'}, inplace=True)

    result = {
        'sales_per_region': sales_per_region.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_regions(request):
    regions = merged_data['region'].unique()
    result = {
        'regions': regions.tolist()
        }
    return JsonResponse(result, safe=False)

def get_years(request):
    years = merged_data['order_date'].dt.year.unique()
    result = {
        'years': years.tolist()
        }
    return JsonResponse(result, safe=False)

def get_sales_per_region_per_month(request, region, year):

    merged_data['order_month'] = merged_data['order_date'].dt.month
    merged_data['order_year'] = merged_data['order_date'].dt.year

    filtered_data = merged_data[(merged_data['region'] == region) & (merged_data['order_year'] == year)]

    sales_per_region_per_month = filtered_data.groupby(['region', 'order_year', 'order_month'])['id'].count().reset_index()
    sales_per_region_per_month.rename(columns={'id': 'total_product_sales'}, inplace=True)

    result = {
        'sales_per_region_per_month': sales_per_region_per_month.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_best_sold_product_in_product_category(request):

    best_sold_product_in_product_category = merged_data.groupby(['Category', 'name'])['id'].count().reset_index()
    best_sold_product_in_product_category.rename(columns={'id': 'total_product_sales'}, inplace=True)
    best_sold_product_in_product_category = best_sold_product_in_product_category.sort_values(by=['Category', 'total_product_sales'], ascending=False)
    best_sold_product_in_product_category = best_sold_product_in_product_category.groupby('Category').head(1)


    result = {
        'best_sold_product_in_product_category': best_sold_product_in_product_category.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_Departmens(request):
    departments = merged_data2['dept_name'].unique()
    result = {
        'departments': departments.tolist()
        }
    return JsonResponse(result, safe=False)

def get_Salary_Per_Employee_Per_Department(request, department):
    filtered_data = merged_data2[(merged_data2['dept_name'] == department)]
    salary_per_employee_per_department = filtered_data.groupby(['dept_name', 'emp_fname', 'emp_lname'])['salary'].sum().reset_index()
    result = {
        'salary_per_employee_per_department': salary_per_employee_per_department.to_dict('records')
    }
    return JsonResponse(result, safe=False)



# if __name__ == "__main__":
#     sales_data = get_sales_per_region_per_month(null, 'Noord', 2019)
#     print(sales_data)
