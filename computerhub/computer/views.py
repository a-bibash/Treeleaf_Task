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



def update(request,id):
    computer_up= Computer.objects.get(id=id)
    computer = ComputerSpecification.objects.all()
    context = {'computer':computer}
    
    if request.method =='POST':
        data = request.POST
        computer_code = data.get("computer_code")
        computer = data.get("computer")
        quantity = int(data.get("quantity"))
        unit_rate =int(data.get("unit_rate"))
                
        computer_name = ComputerSpecification.objects.get(brand=computer)
        
        
        computer_up.computer_code = computer_code
        computer_up.computer = computer_name
        computer_up.quantity = quantity
        computer_up.unit_rate = unit_rate
        
        computer_up.save()
            
        return redirect('/')
    return render(request , 'update.html',context)


def delete(request,id):
    computer_del= Computer.objects.get(id=id)
    computer_del.delete()
    return redirect('/')


