from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=False, default=timezone.now)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


