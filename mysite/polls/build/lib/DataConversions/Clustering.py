import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from .DBConnectie import DBConn
from django.http import JsonResponse

def get_cluster(request):
    df1 = DBConn.toDf(DBConn.F_Order_dates)
    df2 = DBConn.toDf(DBConn.F_Order_FactSUP)
    df = pd.merge(df1, df2, left_on="order_date", right_on="Date", how='inner')
    # df = DBConn.toDf(DBConn.F_Order_FactSUP)
    data = df.copy()

    features = ["month", "Region"]

    le = preprocessing.LabelEncoder()
    for feature in features:
        if data[feature].dtype == 'object':
            data[feature] = le.fit_transform(data[feature])

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[features])

    X = pd.DataFrame(scaled_features, columns=features)

    print(X)

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
