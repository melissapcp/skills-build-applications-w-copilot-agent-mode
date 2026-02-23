from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class APIRootTest(APITestCase):
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

class UserTest(APITestCase):
    def test_create_user(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'pass'}
        response = self.client.post('/users/', data)
        self.assertEqual(response.status_code, 201)

class TeamTest(APITestCase):
    def test_create_team(self):
        data = {'name': 'Test Team'}
        response = self.client.post('/teams/', data)
        self.assertEqual(response.status_code, 201)

class ActivityTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
    def test_create_activity(self):
        data = {'user_id': self.user.id, 'activity_type': 'Running', 'duration': 30}
        response = self.client.post('/activities/', data)
        self.assertEqual(response.status_code, 201)

class LeaderboardTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
    def test_create_leaderboard(self):
        data = {'user_id': self.user.id, 'score': 100}
        response = self.client.post('/leaderboard/', data)
        self.assertEqual(response.status_code, 201)

class WorkoutTest(APITestCase):
    def test_create_workout(self):
        data = {'name': 'Test Workout', 'description': 'A test workout'}
        response = self.client.post('/workouts/', data)
        self.assertEqual(response.status_code, 201)
