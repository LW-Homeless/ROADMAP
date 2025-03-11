from django.urls import path
from .views import index, about, contact, detail_post

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('detail-post/<int:id>/', detail_post, name='detail_post'),
]
