import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from .DBConnectie import DBConn
from django.http import JsonResponse

def predict_bonus(request):
    df = DBConn.toDf(DBConn.salesSUP)
    data = df

    features = ['Order_Quantity', 'Unit_Price']

    le = preprocessing.LabelEncoder()
    for feature in features:
        if data[feature].dtype == 'object':
            data[feature] = le.fit_transform(data[feature])

    X = data[features]

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)


    labels = kmeans.predict(X)


    centers = kmeans.cluster_centers_


    labels = labels.tolist()

    result = {
        'labels': labels,
        'centers': centers.tolist()
    }
    DBConn.supabase.auth.sign_out()
    return JsonResponse(result, safe=False)
