from django.shortcuts import render
from .models import Contactus
# Create your views here.

def home(request):
   return render(request,'page/home.html')

def contact_us(request):
    if request.method=="POST":
        #get data from the form 
        v_name=request.POST.get('firstname')
        v_email=request.POST.get('email')
        v_subject=request.POST.get('topic')
        v_massage=request.POST.get('message')

        #send it to the database
        v_contact= Contactus(firstname=v_name, email=v_email, topic=v_subject, message=v_massage )
        v_contact.save()
        return render(request, 'page/thank.html')
    else:
        return render(request,'page/contact us.html')


def features(request):
    return render(request,'page/features.html')