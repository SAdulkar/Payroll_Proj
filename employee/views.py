from django.shortcuts import render,HttpResponse,redirect
from employee.models import Employee
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from hashlib import sha256
from django.http import HttpResponse


def index(request):
   cookie = request.COOKIES.get('login') 
   if 'logout' in request.POST:
      print('loging out')
      response = redirect('/')
      response.set_cookie('login', 'false')
      response.set_cookie('username', None)
      return response
   if cookie=='true':
      emp_obj = Employee.objects.get(email = request.COOKIES.get('username'))

      context = {
         'name':emp_obj.username
      }
      return render(request,'index.html',context)
   return render(request,'index.html')

def login(request):
    # cookie = request.COOKIES.get('login') 
    # print('cookie',cookie)
    # to check if user login or not
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       print(username,password)
       emp_obj = Employee.objects.filter(email=username,password=sha256(password.encode('utf-8')).hexdigest())
       if len(emp_obj)==1:
          response = redirect('/')
          response.set_cookie('login', 'true')
          response.set_cookie('username', username)
          return response
       
       elif len(emp_obj)==0:
          
          context ={
             'msg':'Invalid Username and Password!'
          }
          return render(request,'login.html',context)
       else:
          context ={
             'msg':'Internal Server Error'
          }
          return render(request,'login.html',context)
    return render(request,'login.html')


def signup(request):
   if request.method=='POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')
      print(username,password1)
      if password1==password2:
         emp_obj = Employee.objects.filter(email=email)
         if len(emp_obj)>=1:
            return render(request,'sign_up.html',{'msg':'User already exists please login!'})
         emp_obj =Employee(username=username,email=email,password = sha256(password1.encode('utf-8')).hexdigest())
         emp_obj.save()
         return redirect('/')
      else:
         return render(request,'sign_up.html',{'msg':'Create Password and Confirm Password doesnt match'})
   return render(request,'sign_up.html',)
# 