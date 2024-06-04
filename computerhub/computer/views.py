from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
    

def list(request):
    
    list = Computer.objects.all()
    context={'list':list}
    return render(request, 'list.html',context)


def create(request):
    computer = ComputerSpecification.objects.all()
    context = {'computer':computer}
      
    if request.method =='POST':
        data = request.POST
        computer_code = data.get("computer_code")
        computer = data.get("computer")
        quantity = int(data.get("quantity"))
        unit_rate =int(data.get("unit_rate"))
                
        computer_name = ComputerSpecification.objects.get(brand=computer)
        
        Computer.objects.create(
        computer_code = computer_code,
        computer = computer_name,
        quantity = quantity,
        unit_rate =unit_rate,
        )
            
        context = {"computer": computer}
        return redirect('/')
    return render(request , 'create.html', context)


def update(request):
    return render(request , 'update.html')


def delete(request):
    return redirect('/')



