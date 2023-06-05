from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go
from .DBConnectie import DBConn
import pandas as pd
from django.http import JsonResponse




def perform_regression(request):

    sales_order_item = DBConn.toDf(DBConn.sales_order_itemSUP)
    sales_order = DBConn.toDf(DBConn.sales_orderSUP)
    product = DBConn.toDf(DBConn.productSUP)
    employee = DBConn.toDf(DBConn.employeeSUP)

    merged_data = pd.merge(sales_order_item, product, left_on='prod_id', right_on='id')
    merged_data = pd.merge(merged_data, sales_order, left_on='id_x', right_on='id')
    merged_data = pd.merge(merged_data, employee, left_on='sales_rep', right_on='emp_id')

    merged_data['unit_price'] = merged_data['unit_price'].astype(float)
    merged_data['salary'] = merged_data['salary'].astype(float)
    merged_data['total_sales_amount'] = merged_data['unit_price'] * merged_data['quantity_y']

    print(merged_data)


    # Invoervariabele en doelvariabele selecteren
    X = merged_data['salary'].values.reshape(-1, 1)
    y = merged_data['total_sales_amount'].values

    # Trainingsset en testset splitsen
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Regressiemodel initialiseren en trainen
    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)

    # Voorspellingen maken op de testset
    y_pred = regression_model.predict(X_test)

    # Prestaties van het model evalueren
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Plot the regression line and data points
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=X_test.flatten(), y=y_test, mode='markers', name='Data Points'))
    fig.add_trace(go.Scatter(x=X_test.flatten(), y=y_pred, mode='lines', name='Regression Line'))

    fig.update_layout(title='Regression Analysis',
                      xaxis_title='Salary',
                      yaxis_title='Total Sales Amount')

    fig.show()

    print('Mean Squared Error:', mse)
    print('R2 Score:', r2)

    # Create a dictionary with the regression results
    results = {
        'mse': mse,
        'r2': r2
    }

    # Return the results as JSON response
    return JsonResponse(results, safe=False)