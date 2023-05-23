from . import views
from django.urls import path, include

urlpatterns = [
    path('blog',views.blog,name='blog')
    
]