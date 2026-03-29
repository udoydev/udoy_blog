from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
 author = models.ForeignKey(
  settings.AUTH_USER_MODEL,
  on_delete=models.CASCADE,
  related_name='blog'
 )
 title = models.CharField(max_length=200)
 content = models.TextField()
 image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
 image_url = models.URLField(blank=True, null=True)
 video = models.FileField(upload_to='blog_videos/',blank=True,null=True)
 video_url = models.URLField(blank=True, null=True)
 created_at = models.DateTimeField(default=timezone.now)
 updated_at = models.DateTimeField(auto_now=True)
 is_published = models.BooleanField(default=True)
 
 class Meta : 
  ordering = ['-created_at'] 
  
 def __str__(self):
  return f"{self.title} by {self.author.username}"
 