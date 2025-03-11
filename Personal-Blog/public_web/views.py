from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib import messages
from private_web.models import Article
from .forms import ContactForm

# Create your views here.


def index(request):
    # Fetch all objects
    all_post = Article.objects.all()

    # 10 items per page
    paginator = Paginator(all_post, 2)

    # Get current page number from URL
    page_number = request.GET.get("page")

    # Get paginated objects
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/index.html', {'page_obj': page_obj})


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been created successful")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})


def detail_post(request, id):
    try:
        post = Article.objects.get(id_article=id)
        return render(request, 'app/detail-post.html', {'post': post})
    except Article.DoesNotExist:
        return render(request, 'app/error_404.html')


def error_404(request, exception):
    return render(request, 'app/error_404.html', status=404)



