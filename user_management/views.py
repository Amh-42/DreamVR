from django.shortcuts import render
from .models import Tourist, SuperAdmin, HotelAdmin, Booking, Transaction, Notification, Sharing

def create_tourist(request):
    if request.method == 'POST':
        # Process form data
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        tourist_id = request.POST['tourist_id']
        user = User.objects.create_user(username=username, password=password, email=email)
        tourist = Tourist.objects.create(user=user, tourist_id=tourist_id)
        return render(request, 'success.html')
    else:
        return render(request, 'create_tourist.html')

def create_superadmin(request):
    # Similar to create_tourist
    pass

def create_hoteladmin(request):
    # Similar to create_tourist
    pass
