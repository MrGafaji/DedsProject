# import pandas as pd
# import pyodbc
# import json

# aenc = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\smkle\Downloads\aenc.accdb;')

# sales_order_item = pd.read_sql_query("SELECT * FROM sales_order_item", aenc)
# sales_order = pd.read_sql_query("SELECT * FROM sales_order", aenc)
# product = pd.read_sql_query("SELECT * FROM product", aenc)
# merged_data = pd.merge(sales_order_item, product, left_on='prod_id', right_on='id')
# merged_data = pd.merge(merged_data, sales_order[['id', 'region']], left_on='id_x', right_on='id')
# merged_data['unit_price'] = merged_data['unit_price'].astype(float)

# def get_sales_per_region(request):

#     sales_per_region = merged_data.groupby('region')['id'].count().reset_index()
#     sales_per_region.rename(columns={'id': 'total_product_sales'}, inplace=True)

#     result = {
#         'sales_per_region': sales_per_region.to_dict('records')
#     }

#     return json.dumps(result)


# if __name__ == "__main__":
#     sales_data = get_sales_per_region()
#     print(sales_data)