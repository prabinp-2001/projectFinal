from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.http import HttpResponse,HttpResponseRedirect
from app.models import student,courses,courseregistration
from app.form import studentForm,studentForm2
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,'base.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def course(request):
    dict_course={
         'course':courses.objects.all()
    }
    return render(request,'course.html',dict_course)


def profile(request):
     current_user = request.user
     k=courseregistration.objects.filter(user_id=current_user.id)
     return render(request,'profile.html', {"s": k})


def form1(request):
     if (request.method =='POST'):
        ph=request.POST['phoneno']
        em=request.POST['email']
        cn=request.POST['coursename']
        current_user = request.user

        if courseregistration.objects.filter(email=em).exists():
             messages.error(request,'email id already exist')
             return redirect('form1')
        
        elif courseregistration.objects.filter(coursename=cn).exists():
             messages.error(request,'already registered')
             return redirect('form1')
        
        elif courseregistration.objects.filter(phoneno=ph).exists():
             messages.error(request,'phone number already exist')
             return redirect('form1')
        
        else:
            o=courseregistration.objects.create(phoneno=ph,email=em,coursename=cn,user_id=current_user.id)
            o.save()
            messages.success(request,'successfully submitted')
     return render(request,'form1.html')





def edit_profile(request,p):
    d=courseregistration.objects.get(pk=p)
    form=studentForm2(instance=d)
    if (request.method=='POST'):
         form=studentForm2(request.POST,instance=d)
         if(form.is_valid()):
              form.save()
              return profile(request)
    return render(request,'popup.html',{'form':form})


def popup(request):
     return render(request,'popup.html')





def signup(request):
     if(request.method =='POST'):
            username=request.POST['username']
            email=request.POST['email']
            password1=request.POST['password1']
            #Check if user already exists
            if User.objects.filter(username=username).exists():
                    messages.error(request,'Username already exists')
            if User.objects.filter(email=email).exists():
                    messages.error(request,'EmailId already exists')
                    return redirect('signup')
            myuser=User.objects.create_user(username,email,password1)
            myuser.save()
            return base(request)
     return render(request,'signup.html')



# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         # Check if user already exists
#         if User.objects.filter(username=username).exists():
#             return render(request, 'signup.html', {'error': 'Username already exists'})

#         # Create new user
#         myuser = User.objects.create_user(username, email, password)
#         myuser.save()
        
#         # Redirect to another page or return a response
#         return render(request, 'success.html')
    
#     return render(request, 'signup.html')






     

def user_login(request):
    if(request.method =='POST'):
            name=request.POST['n']
            password=request.POST['p']
            user = authenticate(username=name,password=password)
            if user:
                login(request,user)
                return base(request)
            else:
               messages.error(request,'invalid user')
               return redirect('login1')
    return render(request,'login1.html')



def logout1(request):
    logout(request)
    return user_login(request)




# def signup(request):
#     form=UserCreationForm()
#     if (request.method=='POST'):
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return base(request)
#     return render(request,'signup.html',{"form":form})