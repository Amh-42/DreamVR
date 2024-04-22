from django.shortcuts import render
from .models import VRExperience, InteractionPoint

def create_vr_experience(request):
    if request.method == 'POST':
        # Process form data
        superadmin_id = request.POST['superadmin_id']
        title = request.POST['title']
        description = request.POST['description']
        vr_experience = VRExperience.objects.create(superadmin_id=superadmin_id, title=title, description=description)
        return render(request, 'success.html')
    else:
        return render(request, 'create_vr_experience.html')
