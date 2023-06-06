import pandas as pd
from django.http import JsonResponse
from .DBConnectie import DBConn

productVendor = DBConn.toDf(DBConn.productVendorSUP)
Vendor = DBConn.toDf(DBConn.vendorSUP)

merged_data = pd.merge(productVendor, Vendor, left_on='BusinessEntityID', right_on='BusinessEntityID')

def get_amount_sold_products_per_supplier(request):
    qty_sold_products_per_supplier = merged_data.groupby('Name')['OnOrderQty'].sum().reset_index()
    qty_sold_products_per_supplier.rename(columns={'OnOrderQty': 'total_sales_quantity'}, inplace=True)
    qty_sold_products_per_supplier = qty_sold_products_per_supplier[qty_sold_products_per_supplier['total_sales_quantity'] != 0]

    result = {
        'amount_sold_products_per_supplier': qty_sold_products_per_supplier.to_dict('records')
    }
    
    return JsonResponse(result, safe=False)

DBConn.supabase.auth.sign_out()


