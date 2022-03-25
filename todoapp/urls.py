from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('delete/<int:pk>/', views.delete , name='todo-delete'),

]
