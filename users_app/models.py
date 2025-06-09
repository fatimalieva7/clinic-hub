from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(' Если email нет то Необходимо указать номер телефона!')
        if User.objects.filter(email=email).exists():
            raise ValueError('Пользователь с таким email уже существует.')
        user = self.model(email=email)
        user.is_staff = True
        user.is_superuser = True
        return user

    def create_superuser(self, email=None, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user



    def create_user_staff(self, email=None, password=None):
        if not email:
            raise ValueError('Необходимо указать email!')
        if not password:
            raise ValueError('Необходимо указать пароль для сотрудника или партнера клиники!')

        user_staff = self.model(email=email)
        # Устанавливаем пароль через метод set_password
        user_staff.set_password(password)
        user_staff.is_staff = True
        user_staff.is_active = True  # Обязательно активируем сотрудника
        user_staff.save(using=self._db)
        return user_staff

class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE = [
        ('user', 'USER'),
        ('superuser', 'SUPERUSER'),
        ('doc', 'DOC'),
    ]

    email = models.EmailField(unique=True, verbose_name='email')
    username = models.CharField(verbose_name='Никнейм', default=None, blank=True, null=True, max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=25, choices=USER_ROLE, default='user')
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    class Meta:
        indexes = [
            models.Index(fields=['email']),
        ]

class SMSVerification(models.Model):
    email = models.EmailField(verbose_name='Email')
    code = models.CharField(max_length=4, verbose_name='Код')
    is_used = models.BooleanField(default=False, verbose_name='Использован ли код?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания кода')


    def __str__(self):
        return f'email Пользователя: {self.email} Код: {self.code}'

    def is_code_valid(self):
        return not self.is_used and timezone.now() < self.created_at + timedelta(minutes=3)
        # Не больше 3 минут крч проверка)
    class Meta:
        indexes = [
            models.Index(fields=['email', 'code']),
        ]
