from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm

# for mail 
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from .forms import PasswordResetRequestForm
from .models import user

# Create your views here.
def user_reg(request):
 form = RegisterForm(request.POST or None)
 
 if request.method == "POST":
  if form.is_valid():
   user=form.save(commit=False)
   user.role='user'
   user.save()
   messages.success(request,"Account Created Successfully ")
   return redirect('login')
 return render(request, 'register.html',{'form': form})

def user_log(request):
 form = LoginForm(request.POST or None)
 if request.method == 'POST':
    if form.is_valid():
     user = form.user
     login(request,user)
     if user.role == "moderator":
      return redirect("moderator_dash")
     return redirect("user_dash") 
 return render(request, 'login.html',{"form":form})


# USER DASHBOARD
from django.utils import timezone
from datetime import timedelta
from apps.blog.models import Blog 
@login_required
def user_dashboard(request):
# Get current time
    now = timezone.now()
    # Calculate 24 hours ago
    yesterday = now - timedelta(hours=24)
    # Filter blogs created in last 24 hours
    recent_blogs = Blog.objects.filter(created_at__gte=yesterday, is_published=True).order_by('-created_at')

    context = {
        'recent_blogs': recent_blogs,
    }
    return render(request, 'user_dash.html', context)


# MODERATOR DASHBOARD
@login_required
def moderator_dashboard(request):

    if request.user.role != "moderator":
        return redirect("login")

    return render(request, "moderator_dash.html")

# User logout
def user_logout (request):
 logout(request)
 messages.success(request,"User Logout Successfully")
 return redirect('login')

def password_reset(request):
 if request.method == "POST":
  form = PasswordResetRequestForm(request.POST)
  if form.is_valid():
   email = form.cleaned_data['email']
   user_obj=user.objects.get(email=email)
   
   # creates token and uid 
   token = default_token_generator.make_token(user_obj)
   uid = urlsafe_base64_encode(force_bytes(user_obj.pk))
   reset_path = reverse('password_reset_confirm',kwargs={'uid':uid,'token':token})
   reset_link=f"http://{get_current_site(request).domain}{reset_path}"
   
   # send email 
   subject = "Password Reset Request "
   html_body= render_to_string('password_reset_email_template.html',{
    'reset_link':reset_link,
    'user':user_obj,
   })
   sent = send_mail(
    subject,
    'Use an email client that supports HTML.',
    settings.EMAIL_HOST_USER,
    [email],
    html_message=html_body,
    fail_silently=False
    )
   messages.success(request,"We sent you a password reset link ! check your mail ")
   return redirect("password_reset_done")
  else:
   messages.error(request,"Please correct the errors below ")
   
 else:
  form = PasswordResetRequestForm()
  
 return render(request, "password_reset.html", {"form": form})




# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from .forms import SetNewPasswordForm

def password_reset_confirm(request,uid,token):
 try:
  uid = urlsafe_base64_decode(uid).decode()
  user_obj = user.objects.get(pk=uid)
 except(TypeError,user.DoesNotExist,OverflowError,ValueError):
  messages.error(request,"Reset Link expired or invalid")
  return redirect("password_reset")

 # check token availability 
 if not default_token_generator.check_token(user_obj,token):
  messages.error(request,"Reset Link expired or invalid ")
  return redirect("password_reset")
 
 # handle form 
 if request.method == "POST":
  form = SetNewPasswordForm(request.POST)
  if form.is_valid():
   password = form.cleaned_data['password1']
   
   # set new password 
   user_obj.set_password(password)
   user_obj.save()
   messages.success(request , " Password reset successfully ")
   return redirect("password_reset_complete")
 else:
  form = SetNewPasswordForm()
  
 return render(request, "password_reset_confirm.html",{'forms': form})

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def password_reset_complete(request):
 return render(request, "password_reset_complete.html")


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def password_reset_done(request):
 return render(request, "password_reset_done.html")

# # test mail setup 
# def test_mail(request):
#  try:
#   sent=send_mail(
#    subject="SMTP",
#    message="Hello! This is a test email from django ",
#    from_email=settings.EMAIL_HOST_USER,
#    recipient_list=["mdimran095m@gmail.com"],
#    fail_silently=False,
#   )
#   return HttpResponse(f"Email send succuessfully ")
#  except Exception as e:
#   return HttpResponse(f"Error: {e}")