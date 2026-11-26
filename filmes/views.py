from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Filme, Diretor, Categoria


def lista_filmes(request):
    
    filmes_qs = Filme.objects.select_related("diretor", "categoria").all()

    
    busca = request.GET.get("busca", "").strip()
    diretor_id = request.GET.get("diretor", "")
    categoria_id = request.GET.get("categoria", "")

    
    if busca:
        filmes_qs = filmes_qs.filter(titulo__icontains=busca)

    if diretor_id:
        filmes_qs = filmes_qs.filter(diretor_id=diretor_id)

    if categoria_id:
        filmes_qs = filmes_qs.filter(categoria_id=categoria_id)

    
    paginator = Paginator(filmes_qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    diretores = Diretor.objects.all()
    categorias = Categoria.objects.all()

    context = {
        "page_obj": page_obj,
        "diretores": diretores,
        "categorias": categorias,
        "busca": busca,
        "diretor_selecionado": diretor_id,
        "categoria_selecionada": categoria_id,
        "total_resultados": filmes_qs.count(),
    }
    return render(request, "filmes/lista_filmes.html", context)
