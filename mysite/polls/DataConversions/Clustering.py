import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from .DBConnectie import DBConn
from django.http import JsonResponse

def get_cluster(request):
    df = DBConn.toDf(DBConn.salesSUP)
    data = df.copy()

    features = ["Order_Quantity", "Profit"]

    le = preprocessing.LabelEncoder()
    for feature in features:
        if data[feature].dtype == 'object':
            data[feature] = le.fit_transform(data[feature])

    X = data[features]

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    labels = kmeans.predict(X)
    centers = kmeans.cluster_centers_

    data['Cluster'] = labels

    result = {
        'labels': labels.tolist(),
        'centers': centers.tolist(),
        'dataPoints': data[features].to_dict(orient='records')
    }
    DBConn.supabase.auth.sign_out()
    return JsonResponse(result, safe=False)
