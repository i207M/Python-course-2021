from django.urls import path, re_path
from . import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('', views.index, name='index'),
]
