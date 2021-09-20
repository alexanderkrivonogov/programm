from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория коммикса')
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Comics(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название комикса')
    comment = models.TextField(max_length=200, verbose_name='Комментарий', blank=True)
    grade = models.FloatField(default=0, verbose_name='Оценка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='img', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Комикс'
        verbose_name_plural = 'Комиксы'

    def __str__(self):
        return self.name
