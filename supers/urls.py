from django.urls import path
from . import views

urlpatterns = [
    path('', views.Supers_list),
    path('<int:pk>/', views.Super_detail)
]