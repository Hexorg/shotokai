from django.urls import path

from . import views

app_name = 'clubs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:club_id>/', views.club, name='club'),
]