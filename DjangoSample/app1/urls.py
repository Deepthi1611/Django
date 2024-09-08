from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1, name = 'app1'),
    path('test', views.test, name = 'test'),
]