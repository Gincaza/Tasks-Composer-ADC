# Generated by Django 5.2.1 on 2025-05-24

from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(
                default=1,  # Substitua pelo ID de um usuário existente
                on_delete=models.CASCADE,
                related_name='tasks',
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]