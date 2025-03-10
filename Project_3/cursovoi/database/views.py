from os import error

from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def database(request):
    student = Students.objects.order_by('last_name') # сортировка по фамилии
    return render(request, 'database/database.html', {'student': student})

class StudentsDetailView(DetailView):
    model = Students
    template_name = 'database/details_view.html'
    context_object_name = 'student'

class StudentsUpdateView(UpdateView):
    model = Students
    template_name = 'database/students-update.html'

    form_class = StudentsForm

class StudentsDeleteView(DeleteView):
    model = Students
    success_url = '/database/'
    template_name = 'database/students-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create') #переадресация на страницу

        else:
            error = 'Форма была заполнена неверно.'

    form = StudentsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'database/create.html', data)

def create2(request):
    return render(request, 'database/create2.html')