from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, Comment

class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description that is long enough',
            priority='low',
            author=self.user
        )
        self.client.login(username='testuser', password='testpass123')

    def test_create_task(self):
        response = self.client.post(reverse('create'), {
            'title': 'New Test Task',
            'description': 'This is a test description that is long enough.',
            'priority': 'low'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Test Task').exists())

    def test_read_task(self):
        response = self.client.get(reverse('read'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'read_task.html')

    def test_update_task(self):
        response = self.client.post(
            reverse('update', kwargs={'task_id': self.task.task}),
            {
                'title': 'Updated Task',
                'description': 'Updated description that is long enough',
                'priority': 'medium'
            }
        )
        self.assertEqual(response.status_code, 302)
        updated_task = Task.objects.get(task=self.task.task)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.priority, 'medium')

    def test_delete_task(self):
        response = self.client.post(
            reverse('delete', kwargs={'task_id': self.task.task})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(task=self.task.task).exists())

    def test_comment_view(self):
        response = self.client.get(
            reverse('comment', kwargs={'task_id': self.task.task})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment.html')
