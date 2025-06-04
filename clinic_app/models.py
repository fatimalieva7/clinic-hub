from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from users_app.models import User
from doctors_app.models import Doctor


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-имя', default='')
    description = models.TextField(max_length=500, verbose_name='Описание категории', default='Без описания')
    image = models.ImageField(upload_to='categories/', verbose_name='Фото категории', default='categories/default.jpg')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
        # indexes = [
        #     models.Index(fields=['created_at']),
        #     models.Index(fields=['updated_at']),
        # ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='URL-имя')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    website = models.URLField(verbose_name="Сайт", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='clinics', verbose_name='Категория')
    logo = models.ImageField(upload_to='clinic_logos/', blank=True, null=True)
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)],
                                 verbose_name='Рейтинг')

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"
        ordering = ['-rating', 'name']
        indexes = [
            models.Index(fields=['rating']),
            # models.Index(fields=['created_at']),
            models.Index(fields=['is_active']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def update_rating(self):
        reviews = self.reviews.filter(moderation_status='approved')
        if reviews.exists():
            avg = sum([r.rating for r in reviews]) / reviews.count()
            self.rating = round(avg, 1)
            super().save(update_fields=['rating'])


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название услуги')
    slug = models.SlugField(max_length=100, verbose_name='URL-имя', blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание услуги', default='Без описания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',validators=[MinValueValidator(0)])
    duration = models.PositiveSmallIntegerField(verbose_name='Длительность (мин)')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='services', verbose_name='Клиника')
    doctors = models.ManyToManyField(Doctor, related_name='services', verbose_name='Врачи', blank=True)
    image = models.ImageField(upload_to='service_image/', verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активна?')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        unique_together = ('clinic', 'slug')
        # ordering = ['price']
        # indexes = [
        #     models.Index(fields=['created_at']),
        #     models.Index(fields=['updated_at']),
        # ]
class ReviewClinic(models.Model):
    RATING_CHOICES = [
        (1, '1 - Плохо'),
        (2, '2 - Удовлетворительно'),
        (3, '3 - Нормально'),
        (4, '4 - Хорошо'),
        (5, '5 - Отлично'),
    ]

    MODERATION_STATUS = [
        ('pending', 'На модерации'),
        ('approved', 'Одобрен'),
        ('rejected', 'Отклонен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clinic_reviews',
                             verbose_name='Пользователь кто оставил отзыв')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='reviews', verbose_name='Клиника')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Оценка от - 1 до 5')
    text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    moderation_status = models.CharField(max_length=10, choices=MODERATION_STATUS, default='pending',
                                         verbose_name='Статус модерации')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('user', 'clinic')
        # ordering = ['-created_at']
        # indexes = [
        #     models.Index(fields=['created_at']),
        #     models.Index(fields=['updated_at']),
        # ]

    def __str__(self):
        return f"Отзыв от {self.user.email} для {self.clinic.name}"


