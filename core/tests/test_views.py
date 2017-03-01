# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail


class IndexViewTestCase(TestCase):

    def setUp(self):
        """Método que executa antes dos outros métodos"""

        self.navegador = Client() #Simula um navegador
        self.url = reverse('index') #Pegar Url com nome

    def tearDown(self):
        """Método que executa depois dos outros métodos"""

        pass

    def test_status_code(self):
        response = self.navegador.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.navegador.get(self.url)
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTestCase(TestCase):

    def setUp(self):
        """Método que executa antes dos outros métodos"""

        self.navegador = Client() #Simula um navegador
        self.url = reverse('contact') #Pegar Url com nome

    def test_view_ok(self):
        response = self.navegador.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):

        data = {'name':'', 'message':'', 'email': ''}
        response = self.navegador.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_form_ok(self):

        data = {'name':'teste', 'message':'teste', 'email': 'teste@teste.com'}
        response = self.navegador.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django Ecommerce')