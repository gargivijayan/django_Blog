from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about',views.about,name="about"),
    path('recent-posts',views.recentposts,name="recent-posts"),
    path('add',views.add,name="add"),
    path('content/<id>',views.detailed,name="detailed"),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    
]

