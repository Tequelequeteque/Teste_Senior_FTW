import base64
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tasks


class TasksTests(APITestCase):
    def setUp(self) -> None:
        user = 'SUPERUSER'
        password = 'SUPERPASS'
        User.objects.create_superuser(username=user, password=password)
        credentials = base64.b64encode(f'{user}:{password}'.encode('utf-8'))
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(credentials.decode('utf-8')))

    def test_create_task(self):
        """
        Ensure we can create a new task object.
        """
        url = reverse('tasks-list')
        data = {'title': 'New task', 'description': 'New task description', 'status': 'to_do', 'priority': 'low'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 1)
        self.assertEqual(Tasks.objects.get().title, 'New task')

    def test_get_task(self):
        """
        Ensure we can get a task object.
        """
        task = Tasks.objects.create(title='New task', description='New task description', status='to_do', priority='low')
        url = reverse('tasks-detail', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'New task')

    def test_update_task(self):
        """
        Ensure we can update a task object.
        """
        task = Tasks.objects.create(title='New task', description='New task description', status='to_do', priority='low')
        url = reverse('tasks-detail', args=[task.id])
        data = {'title': 'Updated task', 'description': 'Updated task description', 'status': 'in_progress', 'priority': 'high'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tasks.objects.get().title, 'Updated task')
    
    def test_delete_task(self):
        """
        Ensure we can delete a task object.
        """
        task = Tasks.objects.create(title='New task', description='New task description', status='to_do', priority='low')
        url = reverse('tasks-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tasks.objects.count(), 0)

