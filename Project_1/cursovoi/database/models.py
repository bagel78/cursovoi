from django.db import models

class Students(models.Model):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=25)
    father_name = models.CharField('Отчество', max_length=50, blank=True)
    birth_date = models.DateField('Дата рождения')
    gender = models.CharField('Пол', max_length=10)
    phone_number = models.CharField('Телефон', max_length=20, blank=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'