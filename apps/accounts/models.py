from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
 Role_Choices = (
  ('user','User'),
  ('moderator','Moderator'),
  ('staff','Staff'),
  ('admin','Admin'),
 )
 
 role = models.CharField(max_length=20, choices=Role_Choices,default='user')
 full_name = models.CharField(max_length=150)
 email = models.EmailField(unique=True)
 phone = models.CharField(max_length=20, blank=True, null=True)
 
 USERNAME_FIELD = 'email'
 REQUIRED_FIELDS=['username']
 
 def __str__(self):
    return self.username