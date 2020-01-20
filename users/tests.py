from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class CustomUserTests(TestCase):
    ...


class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    """   
    def test_create_user(self):
        print("\n\tTesting creation of user")
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
 """
    def test_create_super_user(self):
        print("\n\tTesting creation of superuser")

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

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                             [0].email, self.email)

    def test_signup_template(self):
        print("\n\tTesting signup template")
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi this shouldnt be on the page')
