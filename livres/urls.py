from django.urls import path
from . import views

urlpatterns = [
    path('', views.livre_list, name='livre_list'),
    path('add/', views.livre_add, name='livre_add'),
    path('<int:pk>/edit/', views.livre_edit, name='livre_edit'),
    path('<int:pk>/delete/', views.livre_delete, name='livre_delete'),
    path('chatbot/', views.chatbot, name='chatbot'),
]