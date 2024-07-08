from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
path('',views.job_list,name='jobs'),
path('<str:id>',views.job_detail,name='details')

]
