from django.contrib.auth import get_user_model
from django.test import TestCase

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

        self.assertEqual(user.username,'will')
        self.assertEqual(user.email,'will@email.com')
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

        self.assertEqual(user.username,'superwill')
        self.assertEqual(user.email,'superwill@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


