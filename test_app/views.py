from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# from .forms import CustomUserCreationForm
from django.contrib import messages
from test_app.forms import RegisterForm,LoginForm
from test_app.models import Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Register.objects.create(
                user=user,
                username=form.cleaned_data['username'],
                age=form.cleaned_data['age'],
                image=form.cleaned_data.get('photo'),
                password1=form.cleaned_data.get('password1'),
                password2=form.cleaned_data.get('password2'),
                email=form.cleaned_data.get('email')
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.success(request, 'Form not valid Please Try Again')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.error(request, 'Welcome '+str(user.username))
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'home.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('login')


# @login_required
def index(request):
    try:
        form=Register.objects.get(user=request.user)
        return render(request,'index.html',{'form':form})
    except:
        messages.error(request, 'Invalid username or password.')
        return redirect('login')

def profile(request):
    form=Register.objects.get(user=request.user)
    return render(request,'profile.html',{'form':form})