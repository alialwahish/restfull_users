from django.shortcuts import render,redirect
from .models import user

def index(request):
    count=1
    return render(request,'semi_restful_users/index.html',{'users' :user.objects ,'count':count})

    
def addUser(request):
    if request.method=='POST':
        user.objects.create(full_name=request.POST['firstName']+" "+request.POST['lastName'] , email=request.POST['email'])
    return render(request,'semi_restful_users/addUser.html')
def distroy(request,id):
    print("trying to delete",id)
    user.objects.get(id=id).delete()
    return redirect('/users')


def show(request,id):
    return render(request,'semi_restful_users/users_view.html',{'users' :user.objects.get(id=id)})



def edit(request,id):
    print("we're in editing")
    upUser= user.objects.get(id=id)
    print(upUser.full_name)
    if request.method=='POST':
        upUser.full_name = request.POST['firstName']+" "+request.POST['lastName']
        upUser.email=request.POST['email']
        upUser.save()
    return render(request,'semi_restful_users/edit.html',{'users' :user.objects.get(id=id)})
     
