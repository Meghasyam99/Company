import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import EmployeeDetails
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from .serializers import EmployeeDetailsSerializer
from .validations import password_hash,password_check
from django.core.mail import send_mail 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string 
from django.core.files.storage import FileSystemStorage

mail=settings.EMAIL_HOST_USER

# Create your views here.
@csrf_exempt
def entry_page(req):
    valid=False
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        emp_obj=EmployeeDetails.objects.get(username=username)
        if password==emp_obj.password:
            response=JsonResponse({'status':'cookie set'})
            response.set_cookie(
                key='logged_in',
                value=True,
                # httponly=True,
                # max_age=20,
                # secure=True,
                # samesite='Strict'
            )
            return response
        else:
            valid=True
            return render(req,'login.html',{'valid':valid})
    return render(req,'login.html',{'valid':valid})


def home(req):
    # return JsonResponse({})
    # if req.COOKIES.get('logged_in')=='True':
    #     return render(req,'home.html')
    # else:
    #     return JsonResponse({'status':'login first'}) 
    # if req.COOKIE.get('Theme')=='Dark':
    #     return JsonResponse({'Background':'Dark'})
    # else:
    #     return JsonResponse({'Background':'Light'})
    # return render(req,'home.html')
    if 'username' in req.session:
        return JsonResponse({'status':'this is home page'})
    else:
        return JsonResponse({'status':'Login first'})

def dark_theme(req):
    response=JsonResponse({'status':'Theme set'})
    response.set_cookie(
        key='Theme',
        value='Dark'
    )
    return response

def logout(req):
    # response=JsonResponse({'status':'Logged-out'})
    # response.delete_cookie('logged_in')
    # return response
    req.session.flush()
    return JsonResponse({'status':'Logged out'})

@csrf_exempt
def register(req):
    json_data=json.loads(req.body)
    json_data["password"]=password_hash(json_data.get('password'))
    new_emp=EmployeeDetailsSerializer(data=json_data)

    if new_emp.is_valid():
        new_emp.save()
        return JsonResponse({'status':'Employee Added'})
    else:
        return JsonResponse(new_emp.errors)

@csrf_exempt
def login(req):
    json_data=json.loads(req.body)
    ip_pass=json_data.get('password')
    emp_obj=EmployeeDetails.objects.get(username=json_data["username"])

    if password_check(json_data.get('password'),emp_obj.password):
        return JsonResponse({'status':'Login successful'})
    else:
        return JsonResponse({'status':'Login Failed'})

@csrf_exempt
def update(req):
    json_data=json.loads(req.body)
    emp_obj=EmployeeDetails.objects.get(username=json_data["username"])
    json_data['password']=password_hash(json_data.get('password'))
    updated_pass=EmployeeDetailsSerializer(emp_obj,data=json_data,partial=True)

    if updated_pass.is_valid():
        updated_pass.save()
        return JsonResponse({'status':'Password updated'})
    else:
        return JsonResponse(updated_pass.errors)


def display(req):
    req.session['username']='syam12'
    return JsonResponse({'status':'Session set!'})

def sending_email(req):
    # send_mail( 
    #     subject = "Test Email from Django", 
    #     message = "Hello, this email is sent using Django.", 
    #     from_email = mail, 
    #     recipient_list = ["meghasyamuppu50@gmail.com"], 
    #     fail_silently=False 
    # ) 
    # return HttpResponse("Email Sent Successfully") 
    # ///////////////////

    # html_content = """ 
    # <h1 style="color:skyblue;">Welcome</h1> 
    # <p>Hello, this email is sent using <b>Django</b>.</p> """ 
    # email = EmailMultiAlternatives( 
    #     subject = "HTML Email Test",
    #     body = "This is a test email." ,
    #     from_email = mail, 
    #     to = ["meghasyamuppu50@gmail.com"],
    # ) 
    # email.attach_alternative(html_content, "text/html") 
    # email.send() 
    # return JsonResponse({"status": "HTML Email Sent"}) 
    # /////////////////////
    
    html_content = render_to_string("mail.html",{"name": "syam"})     
    email = EmailMultiAlternatives(         
        subject="Welcome",         
        body="Welcome to our website.",         
        from_email=mail,         
        to=["lalithsaimeesala123@gmail.com"]     
    )     
    email.attach_alternative(html_content,"text/html")     
    email.send()     
    return HttpResponse("Email Sent") 

@csrf_exempt
def store(req):
    if 'resume' in req.FILES:
        fs=FileSystemStorage(location='media/pdf')
        fs.save(req.FILES['resume'].name,req.FILES['resume'])
        return JsonResponse({'status':'File received'})
    return JsonResponse({'status':'File required'})


def show(req):
    print('iam view')
    return JsonResponse({'status':' request reached '})