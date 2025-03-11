from django.db import models

class Classes(models.Model):
    name = models.CharField('Класс', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Students(models.Model):
    GENDER_CHOICES = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    ]
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=25)
    father_name = models.CharField('Отчество', max_length=50, blank=True)
    birth_date = models.DateField('Дата рождения')
    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField('Телефон', max_length=20, blank=True)
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='Класс')

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return f'/database/{self.id}'

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Teachers(models.Model):
    GENDER_CHOICES = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    ]
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=25)
    father_name = models.CharField('Отчество', max_length=50, blank=True)
    birth_date = models.DateField('Дата рождения')
    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField('Телефон', max_length=20, blank=True)
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='Классное руководство')

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return f'/database/{self.id}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'