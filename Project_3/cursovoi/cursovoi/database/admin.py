from django.contrib import admin
from .models import Students, Classes, Teachers

admin.site.register(Students)
admin.site.register(Classes)
admin.site.register(Teachers)