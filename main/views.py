from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.
def say_hello(request, name, age):
    ages = {
        'dushyant': "19",
        'sarthak': "18"
    }

    return HttpResponse("Age: " + str(age) + " | Reversed Name: " + name[::-1])


def get_post(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'main/dushyant.html', context)





def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')

        if len(phone_number) != 10:
            return HttpResponse('Phone number must be 10 digits long')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken!')
        
        user = User.objects.create_user(username=username, password=password)
        author = Author.objects.create(user=user, name=name, mobile_number=phone_number)

        user.save()
        return HttpResponse('Username: ' + str(username) + 'is now registered!')


    if request.method == 'GET':
        return render(request, 'main/sign_up.html')


# def login(request):
@csrf_exempt
def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponse("User already authenticated")

    if request.method == 'GET':
        return render(request, 'main/sign_in.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # author = Author.objects.get(user=user)
            redirect_url = '/author_profile/' + str(username)
            return redirect(redirect_url)
            # return HttpResponse('User login successful ' + str(user.username))
        else:
            return HttpResponse('User login failed: Invalid credentials')


def sign_out(request):
    if not request.user.is_authenticated:
        return HttpResponse('User is not signed in, so he cannot sign out')

    logout(request)
    return HttpResponse('User has been logged out')


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse('User is not authenticated!')

    current_user = request.user
    author = Author.objects.get(user=current_user)
    return render(request, 'main/profile.html', {'author': author, 'user': current_user})


def create_post(request):
    if not request.user.is_authenticated:
        return HttpResponse('User is not authenticated')

    if request.method == 'POST':
        title = str(request.POST.get('title'))
        content = str(request.POST.get('content'))

        current_user = request.user
        author = Author.objects.get(user=current_user)

        post = Post.objects.create(title=title, body=content, author=author)

    return render(request, 'main/create_post.html')


def view_post(request, pk):
    if not request.user.is_authenticated:
        return HttpResponse('User is not authenticated')

    post = Post.objects.get(pk=int(pk))
    author = post.author
    comments = post.comments.all()


    if request.method == 'POST':
        body = str(request.POST.get('body'))
        current_user = request.user
        current_author = Author.objects.get(user=current_user)
        comment = Comment.objects.create(post=post, author=current_author, body=body)
        
        redirect_url = '/view_post/' + str(pk)
        return redirect(redirect_url)


    
    return render(request, 'main/post.html', {'post': post, 'author': author, 'comments': comments})


def author_profile(request, username):
    user = User.objects.get(username=username)
    author = Author.objects.get(user=user)

    posts = Post.objects.filter(author=author)

    context = {
        'posts': posts,
        'author': author
    }
    return render(request, 'main/author_profile.html', context)


