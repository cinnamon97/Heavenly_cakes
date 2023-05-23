from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse



# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        the_user= ''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, ("login Successful!"))
            #request.session['username']= username

            #if request.session['username']== username:
                
             #   the_user=request.session['username']

            return render(request, 'page/home.html')
            
        else:
            
            messages.success(request, ("You Are Not Registered on Our Website, Try Again..."))
            return render(request, 'members/login_user.html', {})
            
            # Return an 'invalid login' error message.

    else:
        return render(request, 'members/login_user.html', {})

#def logout(request):
#   try:
 #     del request.session['username']
  # except:
   #   pass
  # return messages.success(request, ("You Are logged out"))


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return render(request, 'page/thank.html')
    else:
        form = UserCreationForm()
    return render(request, 'members/register_user.html', {
        'form': form,
    })

