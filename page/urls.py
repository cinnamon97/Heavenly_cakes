from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('contact us',views.contact_us,name="contact us"),
    path('features',views.features,name="features")
]