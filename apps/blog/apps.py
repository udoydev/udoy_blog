from django.apps import AppConfig


class BlogConfig(AppConfig):
    # Use full Python path so Django can import correctly from the nested apps package
    name = 'apps.blog'
