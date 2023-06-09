from django.urls import path
from . import views
from polls.DataConversions import AenC as Sales
from polls.DataConversions import AdventureWorks as AdventureWorks
from polls.DataConversions import BikeStore as Bike
from polls.DataConversions import RandomForest as RandomForest
from polls.DataConversions import Clustering as Clustering
from polls.DataConversions import updateScript as Update
from polls.DataConversions import Regression as Reg
from polls.DataConversions import FrequentItem as FItem

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/statistieken", views.vote, name="statistieken"),
    ##region
    path('getSalesAmountPerRegion/', Sales.get_sales_amount_per_region, name='getSalesAmountPerRegion'),
    path('getSalesPerRegion/', Sales.get_sales_per_region, name='getSalesPerRegion'),
    path('getRegions/', Sales.get_regions, name='getRegions'),
    path('getYears/', Sales.get_years, name='getYears'),
    path('getSalesPerRegionPerMonth/<str:region>/<int:year>/', Sales.get_sales_per_region_per_month, name='getSalesPerRegionPerMonth'),
    path('getBestSoldProductInProductCategory/', Sales.get_best_sold_product_in_product_category, name='getBestSoldProductInProductCategory'),
    path('getDepartments/', Sales.get_Departmens, name='getDepartments'),
    path('getSalaryPerEmployeePerDepartment/<str:department>/', Sales.get_Salary_Per_Employee_Per_Department, name='getSalaryPerEmployeePerDepartment'),
    path('perform_regression/', Reg.perform_regression, name='perform_regression'),
    path('perform_frequentitemset/', FItem.perform_frequentitemset, name='perform_frequentitemset'),


    ##klant
    path('getAgeGroups/', Bike.get_age_groups, name='getAgeGroups'),
    path('getproductpercustomergroup/<str:age_group>/', Bike.get_product_per_customergroup, name='get_product_per_customergroup'),
    path('getmostprofitpercustomergroup/', Bike.get_most_profit_per_customergroup, name='get_most_profit_per_customergroup'),
    path('getBestSoldProductInProductCategoryBike/', Bike.get_best_sold_product_in_product_category, name='getBestSoldProductInProductCategoryBike'),
    ##supplier
    path('getQtySoldProductsPerSupplier/', AdventureWorks.get_qty_sold_products_per_supplier, name='getQtySoldProductsPerSupplier'),
    path('getAmountMoneyPerSupplier/', AdventureWorks.get_amount_money_per_supplier, name='getAmountMoneyPerSupplier'),
    path('getMostSoldProducts/', AdventureWorks.get_most_sold_products, name='getMostSoldProducts'),    
    ##machine learning
    path('predict_bonus/', RandomForest.predict_bonus, name='predict_bonus'),
    path('cluster/', Clustering.get_cluster, name='cluster'),
    
    path('getBestSoldProductInProductCategoryAdventure/', AdventureWorks.get_best_sold_product_in_product_category, name='getBestSoldProductInProductCategoryAdventure'),
    ##update
    path('update/', Update.Update_All_Final_Tables, name='update'),
]
