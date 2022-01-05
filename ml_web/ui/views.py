from django.http import request
from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def show(request):
    
    return render(request,'ui/frontpage.html')


def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created. Now able to Login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    
    context={'form':form}


    return render(request,'ui/register.html',context)
