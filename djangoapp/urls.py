from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='get_data'),  # Endpoint to fetch data from Superset
    path('dashboard/<int:id>/', views.getDashboardCharts, name='dashboard_charts'),  # Endpoint to get dashboard charts
]
