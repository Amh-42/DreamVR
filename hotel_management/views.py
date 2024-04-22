from django.shortcuts import render
from .models import HotelPost

def create_hotel_post(request):
    if request.method == 'POST':
        # Process form data
        hotel_admin_id = request.POST['hotel_admin_id']
        post_text = request.POST['post_text']
        hotel_admin = HotelAdmin.objects.get(hotel_admin_id=hotel_admin_id)
        hotel_post = HotelPost.objects.create(hotel_admin=hotel_admin, post_text=post_text)
        return render(request, 'success.html')
    else:
        return render(request, 'create_hotel_post.html')
