from django.test import TestCase
from django.contrib.auth import get_user_model


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
