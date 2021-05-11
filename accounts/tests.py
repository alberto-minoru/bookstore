from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model()
        new_user = user.objects.create_user(
            username='teste',
            email='teste@dominio.com.br',
            password='teste123'
        )
        self.assertEqual(new_user.username, 'teste')
        self.assertEqual(new_user.email, 'teste@dominio.com.br')
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model()
        new_user = user.objects.create_superuser(
            username='super_adm',
            email='super_adm@dominio.com.br',
            password='super_adm123'
        )
        self.assertEqual(new_user.username, 'super_adm')
        self.assertEqual(new_user.email, 'super_adm@dominio.com.br')
        self.assertTrue(new_user.is_active)
        self.assertTrue(new_user.is_staff)
        self.assertTrue(new_user.is_superuser)


class SignupTests(TestCase):

    username = 'new_user'
    email = 'newuser@email.com'

    def setUp(self) -> None:
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
