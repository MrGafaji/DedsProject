import pandas as pd
from django.http import JsonResponse
from .DBConnectie import DBConn

productVendor = DBConn.toDf(DBConn.productVendorSUP)
Vendor = DBConn.toDf(DBConn.vendorSUP)

merged_data = pd.merge(productVendor, Vendor, left_on='BusinessEntityID', right_on='BusinessEntityID')

def get_qty_sold_products_per_supplier(request):
<<<<<<< HEAD
    amount_sold_products_per_supplier = merged_data.groupby('Name')['StandardPrice'].sum().reset_index()
    amount_sold_products_per_supplier.rename(columns={'StandardPrice': 'total_sales_amount'}, inplace=True)
=======
    qty_sold_products_per_supplier = merged_data.groupby('Name')['OnOrderQty'].sum().reset_index()
    qty_sold_products_per_supplier = qty_sold_products_per_supplier.sort_values(by='OnOrderQty', ascending=False)
    qty_sold_products_per_supplier = qty_sold_products_per_supplier[qty_sold_products_per_supplier['OnOrderQty'] > 0]
    qty_sold_products_per_supplier.rename(columns={'OnOrderQty': 'total_sales_quantity'}, inplace=True)
>>>>>>> 67230644e4dec284651538eb02e906bd32630070

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

DBConn.supabase.auth.sign_out()
