from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(verbose_name='Опыт работы')
    is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


