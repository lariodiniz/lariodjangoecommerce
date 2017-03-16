# coding=utf-8

from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from model_mommy import mommy


class RegisterViewTestCase(TestCase):

    def setUp(self):
        """Método que executa antes dos outros métodos"""

        self.navegador = Client()  # Simula um navegador
        self.register_url = reverse('accounts:register')  # Pegar Url com nome

    def test_register_ok(self):
        data = {'username': 'mestredetudo', 'password1': 'mestre123456',
                'password2': 'mestre123456', 'email': 'teste@teste.com'
                }

        response = self.navegador.post(self.register_url, data)

        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(get_user_model().objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'mestredetudo', 'password1': 'mestre123456', 'password2': 'mestre123456'}
        response = self.navegador.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

    def setUp(self):
        """Método que executa antes dos outros métodos"""

        self.navegador = Client()  # Simula um navegador
        self.url = reverse('accounts:update_user')  # Pegar Url com nome
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123456')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name': 'test', 'email': 'test@test.com'}
        response = self.navegador.get(self.url)

        self.assertEquals(response.status_code, 302)
        self.navegador.login(username=self.user.username, password='123456')
        response = self.navegador.post(self.url, data)
        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        self.user.refresh_from_db()

        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.name, 'test')

    def test_update_user_error(self):
        data = {}
        self.navegador.login(username=self.user.username, password='123456')
        response = self.navegador.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')



class UpdatePasswordTestCase(TestCase):
    def setUp(self):
        """Método que executa antes dos outros métodos"""

        self.navegador = Client()  # Simula um navegador
        self.url = reverse('accounts:update_password')  # Pegar Url com nome
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123456')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {'old_password': '123456', 'new_password1': 'teste1234', 'new_password2': 'teste1234'}
        self.navegador.login(username=self.user.username, password='123456')
        response = self.navegador.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('teste1234'))
















