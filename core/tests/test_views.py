# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

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