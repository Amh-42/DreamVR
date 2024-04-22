from django.db import models
from .user_management.models import HotelAdmin

class HotelPost(models.Model):
    hotel_admin = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed
