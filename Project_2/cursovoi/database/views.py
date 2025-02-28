from django.shortcuts import render
from .models import Students
from .forms import StudentsForm

def database(request):
    student = Students.objects.order_by('last_name') # сортировка по фамилии
    return render(request, 'database/database.html', {'student': student})

def create(request):
    form = StudentsForm()

    data = {
        'form': form
    }

    return render(request, 'database/create.html', data)
