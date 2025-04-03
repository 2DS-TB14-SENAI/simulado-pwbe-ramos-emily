from django.urls import path
from . import views

urlpatterns = [
    path('livros/', view=views.listar_livro, name='listar_livro'),
]