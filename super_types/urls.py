from django.urls import path
from . import views

urlpatterns = [
    path('', views.Super_type_list),
    path('<int:pk>/', views.Super_type_detail)
]