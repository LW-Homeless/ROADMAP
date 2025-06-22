from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .filters import ToDoItemFilter
from .pagination import CustomPageNumberPagination

from .models import ToDoList
from .serializer import CreateItemSerializer, UpdateItemSerializer, ObtainItemSerializer
from .permissions import IsOwner

# Create your views here.


class CreateItem(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    http_method_names = ['post']

    def post(self, request):
        serializer = CreateItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateItem(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    http_method_names = ['put']

    def put(self, request, id_item):
        item = get_object_or_404(ToDoList, id=id_item)

        # check permission by object
        self.check_object_permissions(request, item)

        # set datetime update
        data = request.data.copy()
        data['updateAt'] = timezone.now().date()

        serializer = UpdateItemSerializer(item, data=data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteItem(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    http_method_names = ['delete']

    def delete(self, request, id_item):
        item = get_object_or_404(ToDoList, id=id_item)

        # check permission by object
        self.check_object_permissions(request, item)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObtainItems(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    http_method_names = ['get']

    def get(self, request):
        queryset = ToDoList.objects.filter(user=request.user)

        # Apply filters
        filterset = ToDoItemFilter(request.GET, queryset=queryset)
        if not filterset.is_valid():
            return Response(filterset.errors, status=400)

        queryset = filterset.qs

        # Apply sorting
        ordering = request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('id')  # Default sorting

        # Create pagination instance
        paginator = CustomPageNumberPagination()
        try:
            limit = request.query_params.get('limit')
            if limit is not None:
                paginator.max_page_size = int(limit)  # max_page_size is límit maximum
            result_page = paginator.paginate_queryset(queryset, request)

            serializer = ObtainItemSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except ValueError:
            return Response({"detail": "limit parameter must be an integer number"}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(
                {"detail": "The 'api/todo/listItem/' endpoint requires the following params '?page=1&limit=10'"},
                status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(
                {"detail": "The 'api/todo/listItem/' endpoint requires the following params '?page=1&limit=10'"},
                status=status.HTTP_400_BAD_REQUEST)
