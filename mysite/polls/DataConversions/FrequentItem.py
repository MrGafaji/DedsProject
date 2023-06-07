from .DBConnectie import DBConn
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from django.http import JsonResponse
import matplotlib.pyplot as plt
import seaborn as sns


def perform_frequenitemset(request):

    # Retrieve the dataset from your source (e.g., database, CSV file)
    productVendor = DBConn.toDf(DBConn.productVendor)
    vendor = DBConn.toDf(DBConn.vendor)

    merged_data = pd.merge(productVendor, vendor, left_on='BusinessEntityID', right_on='BusinessEntityID')

    # transactions = merged_data[['BusinessEntityID', 'ProductID']].values.tolist()
    transactions = merged_data.groupby('BusinessEntityID')['ProductID'].apply(list).tolist()


    # Perform one-hot encoding of the transactions
    te = TransactionEncoder()
    te_ary = te.fit_transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    print(transactions[:10])  # Check the first 10 transactions

    # Apply Apriori algorithm to find frequent itemsets
    frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    frequent_itemsets = frequent_itemsets[frequent_itemsets['length'] > 1]

    # Convert the frequent itemsets DataFrame to a list of dictionaries
    frequent_itemsets_list = frequent_itemsets.to_dict(orient='records')
    print(frequent_itemsets_list)

     # Convert frozensets to lists
    for itemset in frequent_itemsets_list:
        itemset['itemsets'] = list(itemset['itemsets'])


    # Extract the itemsets and their support values
    itemsets = [', '.join(str(item) for item in itemset['itemsets']) for itemset in frequent_itemsets_list]
    supports = [itemset['support'] for itemset in frequent_itemsets_list]
    print(itemsets)
    print(supports)

    # sns.set(style='whitegrid')  # Set Seaborn style
    plt.figure(figsize=(10, 6))
    sns.barplot(x=itemsets, y=supports, color='steelblue')
    plt.xticks(rotation=90)
    plt.xlabel('Itemsets')
    plt.ylabel('Support')
    plt.title('Frequent Itemsets')

    # Return the frequent itemsets as a JSON response
    return JsonResponse(frequent_itemsets_list, safe=False)    
    