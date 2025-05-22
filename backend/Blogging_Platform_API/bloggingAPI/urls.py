"""
URL configuration for bloggingAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .API_Blogger.views import GetAllPost, GetPostId, CreatePost, UpdatePost, DeletePost, GetPostSearch


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listAllPost/', GetAllPost.as_view(), name='api/listAllPost'),
    path('api/getPost/<int:id_post>/', GetPostId.as_view(), name='api/getPost'),
    path('api/createPost/', CreatePost.as_view(), name='api/createPost'),
    path('api/updatePost/<int:id_post>/', UpdatePost.as_view(), name='api/updatePost'),
    path('api/deletePost/<int:id_post>/', DeletePost.as_view(), name='api/deletePost'),
    path('api/searchPost/<str:term>/', GetPostSearch.as_view(), name='api/searchPost'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
