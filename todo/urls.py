from django.urls import path
from . import views
from .views import signup, login

urlpatterns = [

    #API end points
    path('api/tasks/', views.task_list),
    path('api/tasks/<int:pk>/', views.task_detail),
    path('api/signup/', signup),
    path('api/login/', login),




# UI pages
    path('', views.index),              
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('task/', views.task_page),
    
]