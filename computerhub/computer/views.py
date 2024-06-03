from django.shortcuts import render,redirect

# Create your views here.
    

def list(request):
    return render(request, 'list.html')


def create(request):
    return render(request , 'create.html')


def update(request):
    return render(request , 'update.html')


def delete(request):
    return redirect('/')

