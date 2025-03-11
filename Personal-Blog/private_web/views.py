from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Article
from public_web.models import Contact
from .forms import ArticleForm

# Create your views here.


@login_required(login_url='login')
def list_post(request):
    # Fetch all objects
    all_article = Article.objects.all()

    # 10 items per page
    paginator = Paginator(all_article, 10)

    # Get current page number from URL
    page_number = request.GET.get("page")

    # Get paginated objects
    page_obj = paginator.get_page(page_number)

    return render(request, 'list_post.html', {'page_obj': page_obj})


@login_required(login_url='login')
def delete_post(request, id):
    post = Article.objects.get(id_article=id)
    post.delete()
    messages.success(request, 'The Article has been deleted successful')
    return redirect('list_post')


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The Article has been created successful")
            return redirect('list_post')
    else:
        form = ArticleForm()

    return render(request, 'edit_post.html', {'form': form})

def edit_post(request, id):
    post = Article.objects.get(id_article=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The Article has been update successful")
            return redirect('list_post')
    else:
        form = ArticleForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


@login_required(login_url='login')
def message(request):
    # Fetch all objects
    all_message = Contact.objects.all()

    # 10 items per page
    paginator = Paginator(all_message, 10)

    # Get current page number from URL
    page_number = request.GET.get("page")

    # Get paginated objects
    page_obj = paginator.get_page(page_number)

    return render(request, 'message.html', {'page_obj': page_obj})


@login_required(login_url='login')
def view_message(request, id):
    id_message = Contact.objects.get(id_message=id)
    return render(request, 'view-message.html', {'message': id_message})


@login_required(login_url='login')
def delete_message(request, id):
    id_message = Contact.objects.get(id_message=id)
    id_message.delete()
    messages.success(request, 'The message has been deleted successful')
    return redirect('message')



def user_login(request):
    storage = messages.get_messages(request)
    storage.used = True

    if request.user.is_authenticated:
        return redirect('list_post')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list_post')  # Redirigir a una página protegida
        else:
            messages.error(request, "Username or password incorrect.")

    return render(request, 'login.html')


@login_required(login_url="login")
def user_logout(request):
    storage = messages.get_messages(request)
    storage.used = True

    logout(request)
    return redirect('login')
