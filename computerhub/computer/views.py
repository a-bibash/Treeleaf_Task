from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View
# Create your views here.
    
class List(View):
    def get(self, request):
        list = Computer.objects.all()
        context={'list':list}
        return render(request, 'list.html',context)

class Create(View):
    def get(self, request):
        computer = ComputerSpecification.objects.all()
        context = {'computer':computer}
        return render(request , 'create.html', context)
        
    def post(self, request):
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
        return redirect('/')
    


class Update(View):
    def get(self,request,id):
        computer = ComputerSpecification.objects.all()
        context = {'computer':computer}
        return render(request , 'update.html',context)
    
    def post(self,request,id):
        data = request.POST
        computer_code = data.get("computer_code")
        computer = data.get("computer")
        quantity = int(data.get("quantity"))
        unit_rate =int(data.get("unit_rate"))
        
        computer_up= Computer.objects.get(id=id)        
        computer_name = ComputerSpecification.objects.get(brand=computer)

        computer_up.computer_code = computer_code
        computer_up.computer = computer_name
        computer_up.quantity = quantity
        computer_up.unit_rate = unit_rate
        
        computer_up.save()
            
        return redirect('/')


class Delete(View):
    def get(self,request,id):
        computer_del= Computer.objects.get(id=id)
        computer_del.delete()
        return redirect('/')


