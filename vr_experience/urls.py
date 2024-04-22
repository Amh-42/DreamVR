from django.urls import path
from . import views

urlpatterns = [
    path('create_vr_experience/', views.create_vr_experience, name='create_vr_experience'),
    # Add more URLs for other views as needed
]
