from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def home(request):
    if request.method=="POST":
        nm=request.POST.get("name")
        rl=request.POST.get("role")
        ex=request.POST.get("experience")
        sal=request.POST.get("salary")
        Employee.objects.create(Name=nm,Role=rl,Experience=ex,Salary=sal)
        
        
    return render(request,"home.html")


def view_page(request):
    data=Employee.objects.all()
    
    return render(request,"view.html",{"datas":data})

def update_page(request,id):
    data=Employee.objects.get(id=id)
    if request.method=="POST":
        
        data.Name = request.POST.get("name")
        data.Role = request.POST.get("role")
        data.Experience = request.POST.get("exp")
        data.Salary = request.POST.get("salary")
        data.save()
        return redirect("view_page") 
        
        

    return render(request, "update.html", {"datas": data})



    





