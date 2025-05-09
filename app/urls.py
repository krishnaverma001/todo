from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:k>/', views.update, name='update'),
    path('delete/<str:k>/', views.delete, name='delete'),
    path('toggle/<str:k>/', views.toggle, name='toggle')
]