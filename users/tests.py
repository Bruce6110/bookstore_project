from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        print("&&&&&&&&&&&&& STARTING TEST_CREATE_USER &&&&&&&&&&&&&")
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        print("&&&&&&&&&&&&& FINISHED &&&&&&&&&&&&&")

    def test_create_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superwill',
            email='superwill@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'superwill')
        self.assertEqual(user.email, 'superwill@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class CustomUserTests(TestCase):
    ...


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi this shouldnt be on the page')
