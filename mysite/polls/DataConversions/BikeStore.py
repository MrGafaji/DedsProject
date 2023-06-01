import pandas as pd
from django.http import JsonResponse
import urllib.parse
from .DBConnectie import DBConn

BikeStore = DBConn.toDf(DBConn.sales)

BikeStore['Date'] = pd.to_datetime(BikeStore['Date'])


def get_age_groups(request):
    age_groups = BikeStore['Age_Group'].unique()
    age_groups = age_groups.tolist()

    result = {
        'age_groups': age_groups
    }

    return JsonResponse(result, safe=False)

def get_product_per_customergroup(request, age_group):
    decoded_age_group = urllib.parse.unquote(age_group)

    product_per_customergroup = BikeStore[BikeStore['Age_Group'] == decoded_age_group].groupby('Product')['Order_Quantity'].sum().reset_index()
    product_per_customergroup = product_per_customergroup.sort_values(by='Order_Quantity', ascending=False)
    product_per_customergroup = product_per_customergroup.head(3)

    result = {
        'product_per_customergroup': product_per_customergroup.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_most_profit_per_customergroup(request):
    most_profit_per_customergroup = BikeStore.groupby('Age_Group')['Profit'].sum().reset_index()

    result = {
        'most_profit_per_customergroup': most_profit_per_customergroup.to_dict('records')
    }

    return JsonResponse(result, safe=False)

def get_best_sold_product_in_product_category(request):
    best_sold_product_in_product_category = BikeStore.groupby(['Product_Category', 'Product'])['Order_Quantity'].sum().reset_index()
    best_sold_product_in_product_category = best_sold_product_in_product_category.sort_values(by=['Product_Category', 'Order_Quantity'], ascending=False)
    best_sold_product_in_product_category = best_sold_product_in_product_category.groupby('Product_Category').head(1)


    result = {
        'best_sold_product_in_product_category': best_sold_product_in_product_category.to_dict('records')
    }

    return JsonResponse(result, safe=False)


# if __name__ == "__main__":
#     sales_data = get_product_per_customergroup()
#     print(sales_data)

