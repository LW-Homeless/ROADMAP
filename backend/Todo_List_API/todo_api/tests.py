from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ToDoList

# Create your tests here.


class ToDoApiTest(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = '12345678'
        self.normal_user = User.objects.create_user(username=self.username, password=self.password)
        self.token = str(RefreshToken.for_user(self.normal_user).access_token)

    def test_get_token(self):
        self.toke = {'username': self.username, 'password': self.password}

        self.url = reverse('token_obtain_pair')

        response = self.client.post(self.url, self.toke, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertTrue(response.data['access'])
        self.assertTrue(response.data['refresh'])

    def test_create_item(self):

        self.data = {
            "id": 1,
            "title": "Buy groceries",
            "description": "Buy milk, eggs, and bread"
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.url = reverse('todo/createItem')
        response = self.client.post(self.url, self.data, format='json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.data['title'])
        self.assertEqual(response.data['description'], self.data['description'])

    def test_update_item(self):
        item = ToDoList.objects.create(
            id=1,
            title='Original title',
            description='Original description',
            user=self.normal_user
        )

        self.data = {
            "title": "test1 update",
            "description": "test1 update",
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.url = reverse('todo/updateItem', kwargs={'id_item': item.id})
        response = self.client.put(self.url, self.data, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['title'], self.data['title'])
        self.assertEquals(response.data['description'], self.data['description'])

    def test_delete_item(self):
        item = ToDoList.objects.create(
            id=1,
            title='Original title',
            description='Original description',
            user=self.normal_user
        )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.url = reverse('todo/deleteItem', kwargs={'id_item': item.id})
        response = self.client.delete(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    '''def test_get_items(self):
        # Crear ítems para testuser
        for i in range(5):
            ToDoList.objects.create(
                title=f"Item {i}",
                description="Descripción",
                user=self.normal_user,
                updatedAt=timezone.now()
            )'''

    def test_obtain_items_success(self):
        # Crear ítems para testuser
        for i in range(5):
            ToDoList.objects.create(
                title=f"Item {i}",
                description="Descripción",
                user=self.normal_user,
                updatedAt=timezone.now()
            )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.url = reverse('todo/ObtainItems') + '?page=1&limit=5'
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 5)  # Solo los del usuario autenticado
        self.assertEqual(len(response.data['results']), 5)
        for item in response.data['results']:
            self.assertIn('title', item)
            self.assertIn('description', item)

    def test_invalid_limit(self):
        # Crear ítems para testuser
        for i in range(5):
            ToDoList.objects.create(
                title=f"Item {i}",
                description="Descripción",
                user=self.normal_user,
                updatedAt=timezone.now()
            )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('todo/ObtainItems') + '?page=1&limit=abc'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.data['detail'], "limit parameter must be an integer number")

    def test_missing_params(self):

        # Crear ítems para testuser
        for i in range(5):
            ToDoList.objects.create(
                title=f"Item {i}",
                description="Descripción",
                user=self.normal_user,
                updatedAt=timezone.now()
            )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        url = reverse('todo/ObtainItems')  # sin parámetros
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            "The 'api/todo/listItem/' endpoint requires the following params '?page=1&limit=10'"
        )
