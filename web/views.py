from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import forms
from models import UserProfile, Category, Page
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = forms.UserForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = forms.UserProfile()
            profile.user = user
            profile.save()

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = forms.UserForm()

        return render(request, 'signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'signin.html')


def index(request):
    user = None
    if request.user.is_authenticated():
        user = request.user

    dicts = {
        'user': user,
    }
    return render(request, 'home.html', dicts)


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.website = request.POST.get('website')
        profile.save()

    dicts = {
        'profile': profile
    }
    return render(request, 'admin/index.html', dicts)


def user_info(request):
    profile = UserProfile.objects.get(user_id=request.user.id)

    dicts = {
        'profile': profile
    }
    return render(request, 'admin/user_info.html', dicts)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/profile/')

    form = forms.PostForm()
    category = Category.objects.get_queryset()

    dicts = {
        'form': form,
        'category': category
    }
    return render(request, 'admin/forms.html', dicts)


@login_required
def manage_category(request):
    category = Category.objects.get_queryset()
    form = forms.CategoryForm()
    dicts = {
        'category': category,
        'form': form
    }
    return render(request, 'admin/category.html', dicts)


@login_required
def add_category(request):
    form = forms.CategoryForm(request.POST)
    form.save()
    category = Category.objects.get_queryset()
    dicts = {
        'category': category
    }
    return render(request, 'admin/category.html', dicts)


@login_required
def del_category(request):
    del_id = request.POST.get('id')
    category = Category.objects.get(id=del_id)
    category.delete()
    categories = Category.objects.get_queryset()
    dicts = {
        'category': categories
    }
    return render(request, 'admin/category.html', dicts)


def index_page(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Page.objects.get_queryset().filter(category_id=category_id)
    user = None
    if request.user.is_authenticated():
        user = request.user
    dicts = {
        'category': category,
        'posts': posts,
        'user': user
    }
    return render(request, 'blog/index.html', dicts)


def post_page(request, post_id):
    post = Page.objects.get(id=post_id)
    user = None
    if request.user.is_authenticated():
        user = request.user
    dicts = {
        'post': post,
        'user': user
    }
    return render(request, 'blog/post.html', dicts)


@login_required
def dashboard(request):
    categories = Category.objects.get_queryset()
    posts = Page.objects.get_queryset()
    users = User.objects.get_queryset()

    dicts = {
        'categories': categories,
        'posts': posts,
        'users': users,
    }

    if request.user.is_superuser:
        return render(request, 'admin/index.html', dicts)
    else:
        return render(request, 'admin/user_info.html', dicts)


@login_required
def post_manage(request):
    if request.user.is_superuser:
        posts = Page.objects.get_queryset()
    else:
        posts = Page.objects.get_queryset().filter(author_id=request.user.id)

    dicts = {
        'posts': posts
    }
    return render(request, 'admin/posts.html', dicts)


@login_required
def change_info(request):
    if request.method == 'POST':
        profile = UserProfile.objects.get(user_id=request.user.id)
        profile.user.first_name = request.POST['first_name']
        profile.user.last_name = request.POST['last_name']
        profile.website = request.POST['web_site']
        profile.user.save()
        profile.save()

        return HttpResponseRedirect('/user_info/')
    else:
        return HttpResponseRedirect('/user_info/')

