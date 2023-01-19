from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Part
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
    id_list = car.parts.all().values_list('id')
    parts_car_doesnt_have = Part.objects.exclude(id__in=id_list)
    maint_form = MaintForm()
    return render(request, 'cars/detail.html', { 'car':car, 'maint_form':maint_form, 'parts':parts_car_doesnt_have })

def add_maint(request, car_id):
    form = MaintForm(request.POST)
    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.car_id = car_id
        new_maint.save()
    return redirect('detail', car_id=car_id)

def assoc_part(request, car_id, part_id):
    Car.objects.get(id=car_id).parts.add(part_id)
    return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
    model = Car
    fields = ['model','make','year','description']
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'year', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

class PartList(ListView):
  model = Part

class PartDetail(DetailView):
  model = Part

class PartCreate(CreateView):
  model = Part
  fields = '__all__'

class PartUpdate(UpdateView):
  model = Part
  fields = ['name', 'purpose']

class PartDelete(DeleteView):
  model = Part
  success_url = '/parts/'