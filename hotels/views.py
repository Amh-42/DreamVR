from django.shortcuts import render
from django.http import HttpResponse

def hotels(request):
    return render(request, 'hotels.html')

def hotel(request, pk):
    return HttpResponse('single hotel'+ " " + str(pk))