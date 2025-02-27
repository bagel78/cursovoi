from django.urls import path
from . import views

urlpatterns = [
    path('', views.database, name='database'),
    path('create', views.create, name='create')
]

