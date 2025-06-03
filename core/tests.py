from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import CustomUser

class CoreViewsTestCase(TestCase):
    """
    Testes para as views principais do app core.

    Esta classe cobre testes das páginas principais e do comportamento de autenticação.
    """

    def setUp(self):
        """
        Configura o client de teste para cada teste.
        """
        self.client = Client()

    def test_home_page(self):
        """
        Testa se a página inicial ('home') carrega corretamente.

        Verifica se o status HTTP é 200 e se o template correto é utilizado.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_page(self):
        """
        Testa se a página de login carrega corretamente.

        Verifica se o status HTTP é 200 e se o template correto é utilizado.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_page(self):
        """
        Testa se a página de registro carrega corretamente.

        Verifica se o status HTTP é 200 e se o template correto é utilizado.
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_dashboard_page_redirect_for_unauthenticated(self):
        """
        Testa se um usuário não autenticado é redirecionado ao acessar o dashboard.

        O usuário deve ser redirecionado para a página de login.
        """
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/dashboard/')

    def test_dashboard_page_authenticated(self):
        """
        Testa se usuários autenticados conseguem acessar o dashboard normalmente.

        Cria um usuário de teste, faz login e verifica se o dashboard é acessível.
        """
        user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Faz a requisição autenticada
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
