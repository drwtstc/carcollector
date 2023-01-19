from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import MaintForm

#for the inital response
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars':cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    maint_form = MaintForm()
    return render(request, 'cars/detail.html', { 'car':car, 'maint_form':maint_form })

def add_maint(request, car_id):
    form = MaintForm(request.POST)
    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.car_id = car_id
        new_maint.save()
    return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'