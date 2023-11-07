from django.urls import path,include
from .views import *
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"),
    path("publish",publish,name="publish"),
    path('dashboard', dashboard, name='dashboard'),
    
    path("delete_publish/<int:pk>", delete_publish, name="delete_publish"),
    path("edit_publish/<int:pk>", edit_publish, name="edit_publish"),
    
    path('work/<str:pk>', viewWork, name='work'),
    
    path("login", login_page, name="login"),
    path("signup", signup, name="signup"),
    path("logout", logout_page, name="logout"),




    
      
    
]

# handler404 = 'home.views.custom_404'
