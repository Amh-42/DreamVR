from django.db import models
from django.contrib.auth.models import User

class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tourist_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class SuperAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    superadmin_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class HotelAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel_admin_id = models.CharField(max_length=20, unique=True)
    hotel_id = models.CharField(max_length=20)
    # Add other fields as needed

class Booking(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    hotel_admin = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class Transaction(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class Notification(models.Model):
    recipient = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    notification_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class Sharing(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    share_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed
