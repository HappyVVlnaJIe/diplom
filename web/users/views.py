from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def root_view(request):
    response = redirect('/profile')
    return response

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html')

@login_required
def business_trip_view(request):
    return render(request, 'profile/business_trip.html')

@login_required
def documents_view(request):
    return render(request, 'profile/documents.html')