from django.shortcuts import render,redirect
from .forms import StudentRegister
from .models import Student
from django.contrib import messages
# Create your views here.


def add(request):
    student = Student.objects.all()
    form = StudentRegister()
    if request.method == 'POST':
        form = StudentRegister(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,'student':student}
    return render(request,'add.html',context)


def update(request,pk):
    data = Student.objects.get(id=pk)
    form = StudentRegister(instance=data)
    if request.method == 'POST':
        form = StudentRegister(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
        return redirect('add')
    return render(request,'update.html',{'form':form})


def delete(request,pk):
    data = Student.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('/')


