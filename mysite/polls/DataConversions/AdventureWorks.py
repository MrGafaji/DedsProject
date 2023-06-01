import pandas as pd
from django.http import JsonResponse
from .DBConnectie import DBConn

productVendor = DBConn.toDf(DBConn.productVendorSUP)
Vendor = DBConn.toDf(DBConn.vendorSUP)

merged_data = pd.merge(productVendor, Vendor, left_on='BusinessEntityID', right_on='BusinessEntityID')

def get_amount_sold_products_per_supplier(request):
    amount_sold_products_per_supplier = merged_data.groupby('Name')['StandardPrice'].sum().reset_index()
    amount_sold_products_per_supplier.rename(columns={'StandardPrice': 'total_sales_amount'}, inplace=True)

    result = {
        'amount_sold_products_per_supplier': amount_sold_products_per_supplier.to_dict('records')
    }
    
    return JsonResponse(result, safe=False)


