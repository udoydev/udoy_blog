from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import user


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name',
        }),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your contact number',
        }),
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
    )

    class Meta:
        model = user
        fields = [
            'full_name',
            'email',
            'phone',
            'username',
            'password1',
            'password2',
        ]

    # Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and user.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            if not phone.isdigit():
                raise forms.ValidationError("Phone number must contain only digits")
            if len(phone) < 11:
                raise forms.ValidationError("Phone number must be at least 11 digits")
        return phone
       
       
class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password"
        })
    )
    
    def clean(self):
     cleaned_data = super().clean()
     email = cleaned_data.get("email")
     password = cleaned_data.get("password")
     
     if email and password:
      user = authenticate(email=email,password=password)
      if user is None:
       raise forms.ValidationError("Invalid email or password ")
     
      self.user = user 
     
     return cleaned_data
    
    
#  password reset 
class PasswordResetRequestForm(forms.Form):
 email=forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={
  "class":"form-control",
  "placeholder":"Enter your email",
 }))
 
 def clean_email(self):
  from .models import user
  email = self.cleaned_data.get("email")
  if not user.objects.filter(email=email).exists():
   raise forms.ValidationError("No account found with this email .")
  return email
 
 
class SetNewPasswordForm(forms.Form):
 password1 = forms.CharField(widget=forms.PasswordInput(attrs={
  'class':'form-control',
  'placeholder': ' Enter new password'
 }))
 password2 = forms.CharField(widget=forms.PasswordInput(attrs={
  'class':'form-control',
  'placeholder':'confirm your password ',
 }))
 
 def clean(self):
    cleaned_data = super().clean()
    p1 = cleaned_data.get("password1")
    p2 = cleaned_data.get("password2")
    
    if p1 and p2 and p1 != p2 : 
     raise forms.ValidationError("passwords do not match")
    
    return cleaned_data