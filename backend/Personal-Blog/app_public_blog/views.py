from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import DatabaseError
from .models import Contact, Article
from .form import ArticleForm, ContactForm, CustomAuthForm


# Create your views here.


def home(request):
    try:
        list_article = Article.objects.all()

        paginator = Paginator(list_article, 10)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(request, 'home.html', {'page_obj': page_obj})
    except DatabaseError:
        return render(request, '400.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'The message has been created successfully')
                return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    except DatabaseError:
        return render(request, '400.html')


def article_read_view(request, id_article):
    try:
        article = Article.objects.get(id_article=id_article)
        return render(request, 'article_read.html', {'article': article})
    except DatabaseError:
        return render(request, '400.html')

# Admin Web


@login_required(login_url='login')
def dashboard_view(request):
    try:
        list_article = Article.objects.all()

        paginator = Paginator(list_article, 10)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(request, 'admin_template/dashboard.html', {'page_obj': page_obj})
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def update_article_view(request, id_article):
    try:
        article = Article.objects.get(id_article=id_article)

        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                messages.success(request, 'The message has been updated successfully')
                return redirect('dashboard')
        else:
            form = ArticleForm(instance=article)
        return render(request, 'admin_template/article.html', {'form': form})
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def delete_article_view(request, id_article):
    try:
        article = Article.objects.get(id_article=id_article)
        article.delete()
        messages.success(request, 'The message has been deleted successfully')
        return redirect('dashboard')
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def message_view(request):
    try:
        list_message = Contact.objects.all()

        paginator = Paginator(list_message, 10)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        return render(request, 'admin_template/message.html', {'page_obj': page_obj})
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def delete_message_view(request, id_message):
    try:
        message = Contact.objects.get(id_message=id_message)
        message.delete()
        messages.success(request, 'The message has been deleted successfully')
        return redirect('message')
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def message_view_view(request, id_message):
    try:
        message = Contact.objects.get(id_message=id_message)
        return render(request, 'admin_template/message_view.html', {'message': message})
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def article_view(request):
    try:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'The article has been created successful')
                return redirect('article')
        else:
            form = ArticleForm()
        return render(request, 'admin_template/article.html', {'form': form})
    except DatabaseError:
        return render(request, '400.html')


@login_required(login_url='login')
def article_view_view(request, id_article):
    try:
        article = Article.objects.get(id_article=id_article)
        return render(request, 'admin_template/ViewArticle.html', {'article': article})
    except DatabaseError:
        return render(request, '400.html')


def custom_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            if request.method == 'POST':
                form = CustomAuthForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        messages.error(request, 'Incorrect Username or password')
            else:
                form = CustomAuthForm()
            return render(request, 'admin_template/login.html', {'form': form})
    except DatabaseError:
        return render(request, '400.html')


def custom_logout(request):
    logout(request)
    return redirect('login')


# Error Pages
def error404_view(request):
    return render(request, '404.html', status=404)
