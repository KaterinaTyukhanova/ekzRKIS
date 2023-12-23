from django.contrib.auth.models import AbstractUser
from django.db import models

class Tovar(models.Model):
    name = models.CharField(blank=False, verbose_name='Название товара', max_length=50)
    information = models.TextField(blank=False, verbose_name='Информация о товаре (описание)', max_length=250)
    price = models.DecimalField(blank=True, verbose_name='Стоимость товара', max_digits=10, decimal_places=2, default=0.00)
    tovar_photo = models.ImageField(upload_to='images/', verbose_name='Изображение товара', blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    photo = models.ImageField(upload_to='images/', verbose_name='Фото пользователя', blank=True)

