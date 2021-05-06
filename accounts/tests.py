from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView


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


class SignupPageTests(TestCase):

    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
