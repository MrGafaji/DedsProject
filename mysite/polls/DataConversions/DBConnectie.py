import pandas as pd
import pyodbc
import os
from django.http import JsonResponse
from supabase import create_client, Client
from pandas import json_normalize
import json

class DBConn:

    url: str = 'https://cglhcfmkwabxrvlfuqwb.supabase.co/'
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNnbGhjZm1rd2FieHJ2bGZ1cXdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQxNDk2MzUsImV4cCI6MTk5OTcyNTYzNX0.h-qRysp76hKecbDCjdLaZP03wOaAQ_sl-6_vQ1odb7M"
    supabase: Client = create_client(url, key)
    data = supabase.auth.sign_in_with_password({"email": "outdoorfusion@gmail.com", "password": "Admin123"})

    sales_order_itemSUP = supabase.table('salesOrderItem').select('*').execute().json()
    sales_orderSUP = supabase.table('SalesOrders').select('*').execute().json()
    productSUP = supabase.table('product2').select('*').execute().json()
    employeeSUP = supabase.table('Employee').select('*').execute().json()
    departmentSUP = supabase.table('Department').select('*').execute().json()
    bonusSUP = supabase.table('Bonus').select('*').execute().json()
    product1SUP = supabase.table('Product1').select('*').execute().json()
    productVendor = supabase.table('ProductVendor').select('*').execute().json()
    productionProduct = supabase.table('ProductionProduct').select('*').execute().json()
    sales = supabase.table('Sales').select('*').execute().json()
    salesOrderDetail = supabase.table('SalesOrderDetail').select('*').execute().json()
    salesOrderHeader = supabase.table('SalesOrderHeader').select('*').execute().json()
    vendor = supabase.table('Vendor').select('*').execute().json()

    def toDf(tabel):
        d = json.loads(tabel)
        df = json_normalize(d, 'data')
        return df