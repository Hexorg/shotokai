from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
app_name = 'member_content'
urlpatterns = [
    url('login', auth_views.LoginView.as_view(template_name='member_content/login_failed.html'), name='login'),
    url('register', views.register, name='register'),
    url('logout', auth_views.LogoutView.as_view(), name='logout'),
    url('reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url('', views.index, name='index'),
]