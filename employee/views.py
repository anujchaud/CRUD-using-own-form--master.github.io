from django.shortcuts import render,redirect
from .models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.

def add_view(request):
    if request.method=="POST" or request.method=="FILES":
        name = request.POST.get('name','NA')
        image = request.FILES.get('image',"NA")
        email = request.POST.get('email','NA')
        mobile = request.POST.get('mobile','NA')
        address = request.POST.get('address','NA')
        city = request.POST.get('city','NA')
        # print('Name',name,"Email",email,'Mobile',mobile,"address",address,"city",city,"image",image,"<---------------")
        emp = Employee.objects.create(name=name,image=image,email=email,mobile=mobile,address=address,city=city)
        emp.save()
        messages.success(request, "Employee Added Successfully...")
    
    resp = render(request,'employee/add.html')
    return resp


def show_view(request):
    user_list=Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 4)
    try:
        emp = paginator.page(page)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp = paginator.page(paginator.num_pages)
    d={'emp':emp}
    resp = render(request,'employee/showall.html',context=d)
    return resp


def view_employee(request,eid):
    emp=Employee.objects.get(id=eid)
    d={'emp':emp}
    resp = render(request,'employee/view.html',context=d)
    return resp


def update_view(request,eid):
    data = Employee.objects.get(id=eid)
    if request.method=="POST":
        data.name = request.POST.get('name')
        data.image = request.FILES.get('image',data.image)
        data.email = request.POST.get('email')
        data.mobile = request.POST.get('mobile')
        data.address = request.POST.get('address')
        data.city = request.POST.get('city')
        # print(data.address,"<Update record--........................>")
        # print(image,"<--------------")
        data.save()
        return redirect('/')
    d={'data':data}
    resp = render(request,'employee/update.html',context=d)
    return resp

def delete_view(request,eid):
    data= Employee.objects.get(id=eid)
    data.delete()   
    return redirect('/')    