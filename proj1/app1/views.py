from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.

def StudentView(request):
    form=StudentForm()
    template_name='app1/form.html'
    context={'form': form}

    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            r=form.cleaned_data['rn']
            nm=form.cleaned_data['name']
            ad=form.cleaned_data['adr']
            f=form.cleaned_data['fees']
            ct=form.cleaned_data['city']
            s=Student(rn=r,name=nm,adr=ad,fees=f,city=ct)
            print(s)
            s.save()
               
    return render(request,template_name,context)
    
