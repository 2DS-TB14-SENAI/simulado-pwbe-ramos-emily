from django.shortcuts import render
from .models import Livro


#listar
def listar_livro(request):
    livros = Livro.objects.all()
    return render(request, 'templates/livros.html', {'livros': livros})


