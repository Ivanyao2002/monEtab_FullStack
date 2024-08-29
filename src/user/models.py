from django.db import models

# Create your models here.

class UserModel(models.Model):
    pseudo = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pseudo

    class Meta:
        ordering = ['-id']
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'