from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'video', 'is_published', 'image_url', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter blog title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your blog content here...',
                'rows': 6
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if video.size > (50 * 1024 * 1024):
                raise forms.ValidationError("Video file too large (max 50 MB)")
            if not video.content_type.startswith('video'):
                raise forms.ValidationError("Uploaded file is not a video")
        return video

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > (5 * 1024 * 1024):
                raise forms.ValidationError("Image file too large (max 5 MB)")
            if not image.content_type.startswith('image'):
                raise forms.ValidationError("Uploaded file is not an image")
        return image