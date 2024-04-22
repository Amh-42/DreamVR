from django.urls import path
from . import views

urlpatterns = [
    path('create_hotel_post/', views.create_hotel_post, name='create_hotel_post'),
    # Add more URLs for other views as needed
]
