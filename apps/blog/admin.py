from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # Columns to display in list view
    list_display = ('id', 'title', 'author', 'is_published', 'created_at', 'updated_at')
    
    # Clickable columns
    list_display_links = ('id', 'title')
    
    # Filters on the sidebar
    list_filter = ('is_published', 'author', 'created_at', 'updated_at')
    
    # Searchable fields
    search_fields = ('title', 'content', 'author__username', 'author__email')
    
    # Ordering
    ordering = ('-created_at',)
    
    # Fields editable directly in list view
    list_editable = ('is_published',)
    
    # Fieldsets: organize the form view
    fieldsets = (
        ('Blog Details', {
            'fields': ('title', 'content', 'image', 'image_url', 'video', 'video_url')
        }),
        ('Publication', {
            'fields': ('is_published', 'author')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # collapsible section
        }),
    )
    
    # Read-only fields
    readonly_fields = ('created_at', 'updated_at')
    
    # Automatically set author when creating in admin
    def save_model(self, request, obj, form, change):
        if not change:  # only set on creation
            obj.author = request.user
        super().save_model(request, obj, form, change)