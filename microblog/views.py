from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserCreationForm, LoginUserForm, CreatePost
from .models import Post


# Create your views here.
def index(request):
    return HttpResponse("Welcome to site")


@login_required(login_url='login')
def post(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, "microblog/new_dashboard.html", context)


def register(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account created successfully!")
            return redirect('login')
    context = {'form': form}
    return render(request, "microblog/register.html", context)


def login_user(request):
    form = LoginUserForm()
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'microblog/login.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Success!")
    return redirect('login')


@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            # Assign the current user as the author
            post = form.save(commit=False)
            post.author = request.user  # Assuming you're using Django's authentication system
            post.save()
            messages.success(request, "Your Post was created!")
            return redirect('dashboard')
    else:  # Handle GET request
        form = CreatePost()
    context = {'form': form}
    return render(request, 'microblog/create_post.html', context)
