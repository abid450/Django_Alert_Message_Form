from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import SoftTech_Student_id
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
from .models import *
import uuid
from .utils import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def login(request):
    return render(request,'login.html')


# Register form ------------------------------------
@csrf_exempt
def register(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirmpassw = request.POST.get('password2')
        

        if password!=confirmpassw:
            messages.warning(request, 'Password did not Match !') 
            return redirect('/register_c')

        try:
            if User.objects.get(username=usern):
                messages.error(request,'This Username Already Exist')
                return redirect('/register_c')
            
        except:
            pass
        
        try:
            if User.objects.get(email=email):
                messages.error(request, 'This Email Already Exist')
                return redirect('/register_c')
        except:
            pass

            
        user = User.objects.create_user(usern,email,password)
        user.save()    
        messages.success(request, 'You are Successfully Sign Up')
        return redirect('/register_c')
    return render(request, 'register.html')



# Login Form --------------------------------------
def login_page(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request, username=usern, password=passw)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are Successfully Logged in')
            return HttpResponseRedirect('/Registration')
        
        else:
            messages.error(request, 'Invalid Username or Password')
            return HttpResponseRedirect('/login_page')
    else:
        return render(request, 'login.html')

# Alert Form -------------------------------------------------
def alert_message(request):
    
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        age = request.POST['age']
        biography = request.POST['biography']
        course_name = request.POST['course_name']
        interest = request.POST['interest']
        # Error Handle ---------------------------
        if SoftTech_Student_id.objects.filter(email=email).exists():
            messages.error(request, 'This Email Already Exist')
        elif SoftTech_Student_id.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'This Phone Number Already Exist') 
        
        elif len(name)<4:
            messages.warning(request, 'Incorrect Name, Please Enter Your Correct Name')
        
        elif len(email)<22:
            messages.warning(request, 'Invalid This Email, Please Enter Your Email at least 22 of Characters')       

        elif len(phone_number)<11 or len(phone_number)>11:
            messages.warning(request, 'Invalid This Number, Please Enter Your Phone Number at least 11 of Characters Number') 

        else:
            contect = SoftTech_Student_id(name=name,email=email,phone_number=phone_number,age=age,biography=biography,course_name=course_name,interest=interest)
            contect.save()
            #messages.success(request, 'Congratulations🎉🎉🎉 আপনি আমাদের কোর্সে সফল ভাবে এনরোল করেছেন')
            return HttpResponseRedirect('/message_re')
        
    return render(request, 'alert.html')

# Alert Form Redirect -------------------------------------
def message_re(request):
    #messages.success(request,'You are Successfully Enroll Now')
    return render(request, 'redirect.html')