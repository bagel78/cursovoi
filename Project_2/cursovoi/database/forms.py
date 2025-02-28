from .models import Students
from django.forms import ModelForm, TextInput, DateTimeInput

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['last_name', 'first_name', 'father_name', 'birth_date', 'gender', 'phone_number']

        widgets = {
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "father_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "birth_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            "gender": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            })
        }