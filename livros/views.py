from django.shortcuts import render
from .models import Livro
from rest_framework.decorators import api_view


#listar
@api_view(['GET', 'POST'])
def listar_livro(request):
    if request.method == "GET":
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return render(request, 'livros.html', {'livros': livros})
    elif request.method == "POST":
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

