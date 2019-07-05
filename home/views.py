from django.shortcuts import render,redirect
from home.forms import StudentSearchForm
from home.forms import StudentEditModelForm
from home.forms import StudentCreateForm
from home.models import Student
from django.contrib import messages

# Create your views here.

def home_view(request):
    if request.method=='POST':
        search=StudentSearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=Student.objects.filter(student_name__contains=value)
            return render(request,'search.html',{'result':result,'form':StudentSearchForm()})
    else:
        form=StudentSearchForm()
        result=Student.objects.all()
        return render(request,'search.html',{'form':form,'result':result})

def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Successfully!!!',)
    return redirect('/')


def editstudent(request,id):
        student=Student.objects.get(id=id)
        if request.method=="POST":
                modelform=StudentEditModelForm(request.POST,instance=student)
                if modelform.is_valid():
                        modelform.save()
                        return redirect('/')
        else:
                modelform=StudentEditModelForm(instance=student)
                return render(request,'edit.html',{'form':modelform})
def createstudent(request):
        if request.method=="POST":
                form=StudentCreateForm(request.POST)
                if form.is_valid():
                        student=Student.objects.create(student_name=form.cleaned_data.get("student_name"),
                        department=form.cleaned_data.get('department'))
                        student.save()
                        messages.success(request,"Created Successfully")
                        return redirect('/')
        else:
                form=StudentCreateForm(request.POST)
                return render(request,'create.html',{'form':form})

    # form=StudentSearchForm()
    # msg="hello!!"
    # context={'form':form,'msg':msg}
    # return render(request,'home.html',context)