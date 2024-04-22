from django.urls import path
from . import views

urlpatterns = [
    path('create_tourist/', views.create_tourist, name='create_tourist'),
    path('create_superadmin/', views.create_superadmin, name='create_superadmin'),
    path('create_hoteladmin/', views.create_hoteladmin, name='create_hoteladmin'),
    # Add more URLs for other views as needed
]
