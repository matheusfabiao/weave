from datetime import date

from django.contrib.auth.models import User
from django.db import models

LOCALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(
        max_length=30, blank=True, null=True, choices=LOCALITY_CHOICES
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='profile_pics', default='default.jpg'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self) -> str:
        full_name = f'{self.user.first_name} {self.user.last_name}'.strip()
        return full_name or self.user.username

    @property
    def age(self) -> int:
        return date.today().year - self.birth_date.year

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['-created_at']
