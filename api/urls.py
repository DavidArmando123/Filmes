from django.urls import path
from . import views

urlpatterns = [
    path('creat/', views.filmesCreate.as_view(), name='filmescreate'),
    path('alteracoes/<int:pk>/', views.filmesalteracion.as_view(), name='filmesupdatedestroy'),
]