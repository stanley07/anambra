from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BuildingForm
from .models import Building

def register_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            building = form.save(commit=False)
            building.owner_name = form.cleaned_data['owner_name']
            building.save()
            return redirect('building:registration_success')
    else:
        form = BuildingForm()
    return render(request, 'building/registration.html', {'form': form})

def registration_success(request):
    return render(request, 'building/registration_success.html')

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'building/building_list.html', {'buildings': buildings})