import django_filters
from .models import ToDoList


class ToDoItemFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    created_after = django_filters.DateFilter(field_name='createdAt', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='createdAt', lookup_expr='lte')

    class Meta:
        model = ToDoList
        fields = ['title', 'description', 'created_after', 'created_before']