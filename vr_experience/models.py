from django.db import models
from .user_management.models import SuperAdmin

class VRExperience(models.Model):
    superadmin = models.ForeignKey(SuperAdmin, on_delete=models.CASCADE)
    experience_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class InteractionPoint(models.Model):
    vr_experience = models.ForeignKey(VRExperience, on_delete=models.CASCADE)
    interactionpoint_id = models.CharField(max_length=20, unique=True)
    # Add other fields as needed
