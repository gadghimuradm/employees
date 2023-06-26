from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Position(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'


class Employee(models.Model):
    surname = models.CharField(verbose_name='Фамилия', max_length=64)
    name = models.CharField(verbose_name='Имя', max_length=64)
    patronymic = models.CharField(verbose_name='Отчество', max_length=64, default='', blank=True)
    position = models.ForeignKey(to=Position, verbose_name='Должность', related_name='employees',
                                 null=True, on_delete=models.SET_NULL)
    salary = models.IntegerField(verbose_name='Оклад', default=0, validators=[MinValueValidator(0)])
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=1,
                                           validators=[MinValueValidator(14), MaxValueValidator(120)])
    department = models.ForeignKey(to='api.Department', verbose_name='Департамент', related_name='employees',
                                   null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name}{(" " + self.patronymic) if self.patronymic else ""} ({self.age})'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'


class Department(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=128)
    director = models.ForeignKey(to='api.Employee', verbose_name='Директор', related_name='departments',
                                 unique=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.director.department == self:
            self.director.department = self
            self.director.save(update_fields=['department'])

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'департаменты'
