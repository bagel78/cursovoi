from django.urls import path
from . import views

urlpatterns = [
    path('', views.database, name='database'),
    path('create', views.create, name='create'),
    path('create2', views.create2, name='create2'),

    path('<int:pk>', views.StudentsDetailView.as_view(), name='students-detail'),
    path('<int:pk>/update', views.StudentsUpdateView.as_view(), name='students-update'),
    path('<int:pk>/delete', views.StudentsDeleteView.as_view(), name='students-delete'),

]

