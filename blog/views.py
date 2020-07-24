from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm,UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
  # Write database queries to retrieve the data
  posts = Post.objects.all()
  context = {
    'posts':posts
  }
  return render(request,'blog/index.html',context)

def post_detail(request,slug):
  apost = Post.objects.filter(slug = slug).first()
  context = {
    'post':apost
  }
  return render(request,'blog/post-detail.html',context)

@login_required
def createpost(request):
  # You want to capture both GET/POST
  if request.method == 'POST':
    form = PostForm(request.POST)
    form.save()
    messages.success(request,'Yeepee!! Your blog post is LIVE !!')
    return redirect('index')
  else:
    form = PostForm()
  context = {
    'form':form
  }
  return render(request,'blog/createpost.html',context)


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    form.save()
    return redirect('index')
  else:
    form = UserRegisterForm()

  context = {
    'form':form
  }
  return render(request,'registration/register.html',context)