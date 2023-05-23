from . import views
from django.urls import path

urlpatterns = [
    path('cake',views.cake,name='cake'),
    path('cookies',views.cookies,name='cookies'),
    path('strawberries',views.strawberries,name='strawberries'),
    path('cakemenu',views.cakemenu,name='cakemenu'),
    path('koreanmenu',views.koreanmenu,name='koreanmenu')
]