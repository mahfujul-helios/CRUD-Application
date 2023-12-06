from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentsRegistrations
from .models import User
# Create your views here.
def addShow(request):
    if request.method == 'POST':
        fm = StudentsRegistrations(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentsRegistrations()
    else:
        fm = StudentsRegistrations()
    stud= User.objects.all()

    return render(request,"std/addShow.html",{'form':fm,'stu':stud})


#delete data

def deleteData(request,id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')
    





#update data

def updateData(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        fm = StudentsRegistrations(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
    else:
        data = User.objects.get(pk=id)
        fm = StudentsRegistrations(instance=data)

    return render(request, 'std/update.html', {'form': fm})


