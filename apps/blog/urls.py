from django.urls import path
from apps.blog import views


# Placeholder URL patterns to satisfy include(); add real routes here when available.
urlpatterns = [
 path('add/',views.add_blog,name='add_blog'),
 path('list/',views.list,name='list'),
     path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('my_blogs/',views.my_blogs,name='my_blogs'),
    path('detail/<int:id>/', views.blog_detail, name='blog_detail'),
 
]


