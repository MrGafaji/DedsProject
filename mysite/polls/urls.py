from django.urls import path
from . import views
from polls.DataConversions import SalesPerRegion as Sales

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/statistieken", views.vote, name="statistieken"),
    path('getSalesAmountPerRegion/', Sales.get_sales_amount_per_region, name='getSalesAmountPerRegion'),
    path('getSalesPerRegion/', Sales.get_sales_per_region, name='getSalesPerRegion'),
]
