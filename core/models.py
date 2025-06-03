from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Task(models.Model):
    """
    Modelo que representa uma tarefa atribuída a um usuário.

    Attributes:
        title (str): Título da tarefa.
        description (str): Descrição detalhada da tarefa (opcional).
        due_date (date): Data de vencimento da tarefa.
        completed (bool): Indica se a tarefa foi concluída.
        user (CustomUser): Usuário ao qual a tarefa pertence.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        """
        Retorna uma representação em string da tarefa.

        Returns:
            str: O título da tarefa.
        """
        return self.title

class CustomUser(AbstractUser):
    """
    Modelo de usuário customizado que estende o AbstractUser do Django.

    Attributes:
        name (str): Nome completo do usuário (opcional).
    """
    name = models.CharField(max_length=150, blank=True, null=True)
