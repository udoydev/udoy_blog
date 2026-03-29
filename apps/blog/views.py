from django.shortcuts import render,redirect
import mimetypes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog
# Create your views here.
@login_required(login_url='login')
def add_blog(request):
 if request.method == 'POST':
  form = BlogForm(request.POST,request.FILES)
  if form.is_valid():
   blog = form.save(commit=False)
   blog.author = request.user
   # If no file uploaded, use URL
   if not blog.image and form.cleaned_data.get('image_url'):
        blog.image_url = form.cleaned_data['image_url']
   if not blog.video and form.cleaned_data.get('video_url'):
        blog.video_url = form.cleaned_data['video_url']
   blog.save()
   messages.success(request , "Blog post created successfully ")
   return redirect('list')
  else:
   messages.error(request,"Please fix the errors below.")
 else:
  form = BlogForm()
 return render (request,"blog/add_blog.html",{"form":form})

@login_required(login_url='login')
def list(request):
 blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
 return render(request, "blog/list.html", {"blogs": blogs,'is_edit':False})

# My Blogs
# -----------------------------------------------------------------------------
@login_required(login_url='login')
def my_blogs(request):
 blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
 return render(request, "blog/my_blog.html", {"blogs": blogs})
# -----------------------------------------------------------------------------

@login_required(login_url='login')
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    # 🔒 Only owner can delete
    if blog.author != request.user:
        messages.error(request, "Not allowed!")
        return redirect('list')

    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Blog deleted successfully")

    return redirect('my_blogs')

from django.shortcuts import get_object_or_404

@login_required(login_url='login')
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    # 🔒 Only owner can edit
    if blog.author != request.user:
        messages.error(request, "Not allowed!")
        return redirect('list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully")
            return redirect('list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/add_blog.html', {'form': form,'is_edit':True})

# View Full Blog
#----------------------------------------------------------------------------
@login_required(login_url='login')
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    video_url = None
    video_mime = None

    if blog.video:
        video_url = blog.video.url
        video_mime = mimetypes.guess_type(blog.video.name)[0] or 'video/mp4'
    elif blog.video_url:
        video_url = blog.video_url
        video_mime = mimetypes.guess_type(blog.video_url)[0] or 'video/mp4'

    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'video_url': video_url,
        'video_mime': video_mime,
    })
#----------------------------------------------------------------------------