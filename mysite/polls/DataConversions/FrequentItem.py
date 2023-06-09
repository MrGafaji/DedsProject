from .DBConnectie import DBConn
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
from django.http import JsonResponse


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
    supports = frequent_itemsets['support']
    itemsets = frequent_itemsets['itemsets'].astype(str)

   # Prepare data for chart
    chart_data = {
        'itemsets': itemsets.tolist(),
        'supports': supports.tolist()
    }

    # Return JSON response
    return JsonResponse(chart_data)

