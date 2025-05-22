from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Post
from .serializer import GetPostSerializer, PostPostSerializer, PutPostSerializer


# Create your views here.

class GetAllPost(APIView):
    http_method_names = ['get']

    @extend_schema(
        responses=GetPostSerializer(many=True)
    )
    def get(self, request):
        query_set = Post.objects.all()
        serializer = GetPostSerializer(query_set, many=True)
        return Response(serializer.data)


class GetPostId(APIView):
    http_method_names = ['get']

    @extend_schema(
        responses=GetPostSerializer
    )
    def get(self, request, id_post):
        query_set = get_object_or_404(Post, id_post=id_post)
        serializer = GetPostSerializer(query_set)
        return Response(serializer.data)


class GetPostSearch(APIView):
    http_method_names = ['get']

    @extend_schema(
        responses=GetPostSerializer(many=True)
    )
    def get(self, request, term):
        query_set = Post.objects.filter(
            Q(title__icontains=term) |
            Q(content__icontains=term)
        )
        serializer = GetPostSerializer(query_set, many=True)
        return Response(serializer.data)


class CreatePost(APIView):
    http_method_name = ['post']

    @extend_schema(
        responses={201: OpenApiResponse(description='Created')}
    )
    def post(self, request):
        serializer = PostPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(APIView):
    http_method_names = ['put']

    @extend_schema(
        responses={
            200: OpenApiResponse(description='OK'),
            404: OpenApiResponse(description='"No Post matches the given query.'),
        }
    )
    def put(self, request, id_post=None):
        if id_post is not None:
            post = get_object_or_404(Post, id_post=id_post)
            serializer = PutPostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeletePost(APIView):
    http_method_names = ['delete']

    @extend_schema(
        responses={
            204: OpenApiResponse(description='No Content'),
            404: OpenApiResponse(description='Not found')
        }
    )
    def delete(self, request, id_post=None):
        post = get_object_or_404(Post, id_post=id_post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
