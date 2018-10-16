from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    data = models.DateTimeField(auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.user.username
