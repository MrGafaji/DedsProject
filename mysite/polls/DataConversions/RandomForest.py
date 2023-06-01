import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from .DBConnectie import DBConn
from django.http import JsonResponse

def predict_bonus(request):
    df = DBConn.toDf(DBConn.bonusSUP)
    df['bonus_date'] = pd.to_datetime(df['bonus_date'], format='%d-%b-%Y %I:%M:%S %p')
    df['bonus_amount'] = df['bonus_amount'].astype(float)

    X = df.drop(['bonus_amount'], axis=1)
    y = df['bonus_amount']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(df.dtypes)  # Print the data types of DataFrame columns

    clf = RandomForestRegressor(n_estimators=100, max_depth=4, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    result = {
        'Root Mean Squared Error:': rmse
    }

    return JsonResponse(result, safe=False)
