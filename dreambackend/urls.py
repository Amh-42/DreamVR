from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def hotels(request):
    return HttpResponse('Hotels List')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', admin.site.urls),
    path('hotels/', admin.site.urls),
]
