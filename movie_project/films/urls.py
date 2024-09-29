from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_new/', views.new_record, name='add_films')
   # path('animals/', views.animals, name='animals'),
   # path('personal/', views.personal, name='personal')
]
# при указании адреса /create_new (или ссылка по имени add_films) будем вызывать функцию new_record
# views.new_record - будем запускать функцию new_record из файлика views