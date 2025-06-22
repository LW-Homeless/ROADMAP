from django.urls import path
from .views import CreateItem, UpdateItem, DeleteItem, ObtainItems

urlpatterns = [
    path('todo/createItem/', CreateItem.as_view(), name='todo/createItem'),
    path('todo/updateItem/<int:id_item>/', UpdateItem.as_view(), name='todo/updateItem'),
    path('todo/deleteItem/<int:id_item>/', DeleteItem.as_view(), name='todo/deleteItem'),
    path('todo/listItem/', ObtainItems.as_view(), name='todo/ObtainItems')
]
