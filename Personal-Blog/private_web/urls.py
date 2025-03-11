from django.urls import path
from .views import list_post, create_post, delete_post, edit_post, message, view_message, delete_message, user_login, \
    user_logout

urlpatterns = [
    path('', list_post, name='list_post'),
    path('create-post', create_post, name='create_post'),
    path('edit-post<int:id>', edit_post, name='edit_post'),
    path('delete-post/<int:id>', delete_post, name='delete_post'),
    path('message', message, name='message'),
    path('view-message/<int:id>/', view_message, name='view_message'),
    path('delete-message/<int:id>/', delete_message, name='delete_message'),
    path('login', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]
