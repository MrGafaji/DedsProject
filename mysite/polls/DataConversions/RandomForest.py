import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from .DBConnectie import DBConn
from django.http import JsonResponse

def predict_bonus(request):
    df = DBConn.toDf(DBConn.salesSUP)
    data = df

    features = ['Customer_Age', 'Age_Group', 'Customer_Gender', 'Country', 'State', 'Product_Category', 'Sub_Category', 'Product', 'Order_Quantity', 'Unit_Cost', 'Unit_Price']

    le = preprocessing.LabelEncoder()
    for feature in features:
        if data[feature].dtype == 'object':
            data[feature] = le.fit_transform(data[feature])

    target = 'Profit'

    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.3, random_state=1)

    clf = DecisionTreeClassifier()

    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)


    result = accuracy

    return JsonResponse(result, safe=False)
