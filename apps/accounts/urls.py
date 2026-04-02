from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.user_reg,name='registration'),
    path('login/',views.user_log,name="login"),
    path('user_dash/',views.user_dashboard,name="user_dash"),
    path('moderator_dash/',views.moderator_dashboard,name="moderator_dash"),
    path('logout/',views.user_logout,name="logout"),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("home/", views.home, name="home"),
    
    path(
        "password_reset_confirm/<uid>/<token>/",
        views.password_reset_confirm,
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        views.password_reset_complete,
        name="password_reset_complete",
    ),
    path("password_reset_done/", views.password_reset_done, name="password_reset_done"),
    # path('test_mail/', views.test_mail, name='test_mail'),
]
