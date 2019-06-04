from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.index, name='index'),
  path('ckd', views.ckd, name='ckd'),
  path('register', views.register, name='register'),
  path('login', views.login, name='login'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('logout', views.logout, name='logout'),
  path('createNote', views.createNote, name="createNote")

]