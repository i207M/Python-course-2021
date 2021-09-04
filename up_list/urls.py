from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'show/(\d+)/', views.show, name='show'),
    path('', views.index, name='index'),
]
