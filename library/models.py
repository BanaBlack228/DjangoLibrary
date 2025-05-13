from django.db import models
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Название')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год создания')

    def __str__(self):
        return self.title
