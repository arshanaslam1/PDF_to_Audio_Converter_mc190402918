from django.urls import path
from . import views


app_name = 'converter'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreatePDFView.as_view(), name='pdf-create'),
    path('converter/', views.DashboardView.as_view(), name='pdf-home'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
]
