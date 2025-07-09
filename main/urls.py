from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm,logout
from .views import logout_view


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', logout_view,name='logout')


]