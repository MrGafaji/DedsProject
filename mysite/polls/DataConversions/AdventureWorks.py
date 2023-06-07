import pandas as pd
from django.http import JsonResponse
from .DBConnectie import DBConn

productVendor = DBConn.toDf(DBConn.productVendorSUP)
Vendor = DBConn.toDf(DBConn.vendorSUP)
SalesOrderDetail = DBConn.toDf(DBConn.salesOrderDetailSUP)
ProductionProduct = DBConn.toDf(DBConn.productionProductSUP)

merged_data = pd.merge(productVendor, Vendor, left_on='BusinessEntityID', right_on='BusinessEntityID')
merged_data2 = pd.merge(SalesOrderDetail, ProductionProduct, on='ProductID')

def get_qty_sold_products_per_supplier(request):
    qty_sold_products_per_supplier = merged_data.groupby('Name')['OnOrderQty'].sum().reset_index()
    qty_sold_products_per_supplier = qty_sold_products_per_supplier.sort_values(by='OnOrderQty', ascending=False)
    qty_sold_products_per_supplier = qty_sold_products_per_supplier[qty_sold_products_per_supplier['OnOrderQty'] > 0]
    qty_sold_products_per_supplier.rename(columns={'OnOrderQty': 'total_sales_quantity'}, inplace=True)

    result = {
        'qty_sold_products_per_supplier': qty_sold_products_per_supplier.to_dict('records')
    }
    
    return JsonResponse(result, safe=False)

def get_amount_money_per_supplier(request):
    amount_money_per_supplier = merged_data.groupby('Name').apply(lambda x: (x['OnOrderQty'] * x['LastReceiptCost']).sum()).reset_index(name='total_amount_money')
    amount_money_per_supplier = amount_money_per_supplier.sort_values(by='total_amount_money', ascending=False)
    amount_money_per_supplier = amount_money_per_supplier[amount_money_per_supplier['total_amount_money'] > 0]

    result = {
        'amount_money_per_supplier': amount_money_per_supplier.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_most_sold_products(request):
    most_sold_products = merged_data2.groupby('Name')['OrderQty'].sum().reset_index()
    most_sold_products = most_sold_products.sort_values(by='OrderQty', ascending=False)
    most_sold_products = most_sold_products.head(2)
    most_sold_products = most_sold_products[most_sold_products['OrderQty'] > 0]
    most_sold_products.rename(columns={'OrderQty': 'total_sales_quantity'}, inplace=True)

    result = {
        'most_sold_products': most_sold_products.to_dict('records')
    }

    return JsonResponse(result, safe=False)

DBConn.supabase.auth.sign_out()
