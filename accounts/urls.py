from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.AccountRegisterView.as_view(), name='register'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),

]
