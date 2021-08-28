# from crudproj.crudapp.forms import GenderForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from crudapp.forms import EmployeeForm
from .models import EmployeeDetails
# Create your views here.
def insert(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                # return HttpResponse('<h1>Data sent to Database</h1>')
            except:
                pass    
    form=EmployeeForm()
    return render(request, 'index.html', {'form':form})
            


def show(request):
    empdetails=EmployeeDetails.objects.all()
    return render(request, 'show.html', {'empdetails':empdetails})    


def delete(request, id):
    empdetails=EmployeeDetails.objects.get(id=id)
    empdetails.delete()
    return redirect('/show')    


def edit(request, id):
    emps=EmployeeDetails.objects.get(id=id)
    return render(request, 'edit.html', {'emps':emps})    


def update(request, id):
    empdetails=EmployeeDetails.objects.get(id=id)
    empform=EmployeeForm(request.POST, instance=empdetails)
    if empform.is_valid():
        empform.save()
        return redirect('/show')
    return render(request, 'edit.html', {'empdetails':empdetails})