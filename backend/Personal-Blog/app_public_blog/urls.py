from django.urls import path
from django.conf.urls import handler404
from .views import (home, about, contact, dashboard_view, message_view, delete_message_view,
                    message_view_view, article_view, update_article_view,
                    delete_article_view, article_read_view, article_view_view, custom_login, custom_logout, error404_view)

handler404 = error404_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('article/', article_view, name='article'),
    path('article-delete/<int:id_article>', delete_article_view, name='deleteArticle'),
    path('article-update/<int:id_article>', update_article_view, name="updateArticle"),
    path('article-read/<int:id_article>', article_read_view, name='articleRead'),
    path('article-view/<int:id_article>', article_view_view, name='viewArticle'),
    path('message/', message_view, name='message'),
    path('message-view/<int:id_message>', message_view_view, name='messageView'),
    path('message-delete/<int:id_message>', delete_message_view, name='deleteMessage'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
