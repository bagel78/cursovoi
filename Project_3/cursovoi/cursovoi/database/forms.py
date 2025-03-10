from .models import Students, Teachers
from django.forms import ModelForm, TextInput, Select

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['last_name', 'first_name', 'father_name', 'birth_date', 'gender', 'phone_number', 'class_name']

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
            "birth_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date'
            }),
            "gender": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "class_name": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Класс'
            })
        }

class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['last_name', 'first_name', 'father_name', 'birth_date', 'gender', 'phone_number', 'class_name']

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
            "birth_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date'
            }),
            "gender": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "class_name": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Классное руководство'
            })
        }