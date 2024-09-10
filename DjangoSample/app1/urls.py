from django.urls import path
from . import views

urlpatterns = [
    # path('', views.app1, name = 'app1'),
    # path('test', views.test, name = 'test'),
    path('', views.allChai, name = 'allChais'),
    path('<int:chaiId>/', views.chaiDetail, name = 'chaiDetail'),
    path('chai_stores/', views.chaiStore, name = 'chaiStore')
]