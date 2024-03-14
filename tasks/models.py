from django.db import models

class Tasks(models.Model):

    STATUS_CHOICES = (
        ('to_do', 'A fazer'),
        ('in_progress', 'Em progresso'),
        ('done', 'Concluído'),
    )

    PRIORITY_CHOICES = (
        ('urgent', 'Urgente'),
        ('high', 'Alta'),
        ('medium', 'Média'),
        ('low', 'Baixa'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Em progresso')
    priority = models.CharField(max_length=12, choices=PRIORITY_CHOICES, default='Média')
    created_at = models.DateTimeField(auto_now_add=True)
