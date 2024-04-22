from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),
    path('hotel_management/', include('hotel_management.urls')),
    path('vr_experience/', include('vr_experience.urls')),
    # Add more app URLs as needed
]
