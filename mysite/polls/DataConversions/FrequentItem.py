# from .DBConnectie import DBConn
# import pandas as pd
# from mlxtend.frequent_patterns import fpgrowth
# from mlxtend.frequent_patterns import apriori
# from mlxtend.preprocessing import TransactionEncoder
# from django.http import JsonResponse
# import matplotlib.pyplot as plt
# import seaborn as sns
# import json

# def perform_frequentitemset(request):
# #     productVendor = DBConn.toDf(DBConn.productVendor)
# #     vendor = DBConn.toDf(DBConn.vendor)

#     merged_data = pd.merge(productVendor, vendor, on='BusinessEntityID')
    # transactions = merged_data.groupby('BusinessEntityID')['ProductID'].apply(list).tolist()
from .DBConnectie import DBConn
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
from django.http import JsonResponse
import matplotlib.pyplot as plt
import io
import base64

# Assuming you have the data in a DataFrame called 'productVendor'
# with columns 'ProductId' and 'BusinessEntityID'
def perform_frequentitemset(request):

    productVendor = DBConn.toDf(DBConn.productVendor)

# Assuming you have the data in a DataFrame called 'productVendor'
# with columns 'ProductId' and 'BusinessEntityID'
    transactions = productVendor.groupby('ProductID')['BusinessEntityID'].apply(list).values.tolist()

# Convert the transaction data into a one-hot encoded format
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    productVendor = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
    frequent_itemsets = apriori(productVendor, min_support=0.01, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    frequent_itemsets = frequent_itemsets[frequent_itemsets['length'] > 1]
    
    print(frequent_itemsets)
# Convert the frequent itemsets DataFrame to JSON
    # frequent_itemsets_json = frequent_itemsets.to_json(orient='records')
    # Extract the support values and itemsets
    supports = frequent_itemsets['support']
    itemsets = frequent_itemsets['itemsets'].astype(str)

   # Prepare data for chart
    chart_data = {
        'itemsets': itemsets.tolist(),
        'supports': supports.tolist()
    }

    # Return JSON response
    return JsonResponse(chart_data)

