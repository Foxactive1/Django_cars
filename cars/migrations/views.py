from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm, CarSearchForm

def cars_list(request):
    form = CarSearchForm(request.GET)
    cars = Car.objects.all().order_by('brand__name')
    
    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
    
    return render(request, 'cars/list.html', {'cars': cars, 'form': form})

def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = CarForm()
    return render(request, 'cars/new.html', {'form': form})

def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/edit.html', {'form': form})

def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('cars_list')