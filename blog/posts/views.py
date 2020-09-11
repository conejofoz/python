from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When



class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 2
    context_object_name = 'posts' # objeto que vai para o html

    # sobreescrever o método para ordenar os registros da maneira que quiser
    def get_queryset(self):
        qs = super().get_queryset()
        # ordenar por id em ordem decrescente e filtrar somente os posts que estão publicados
        qs = qs.order_by('-id').filter(publicado_post=True)
        # contar somente comentários que estão publicados
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs



class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    # como está herdando de PostIndex vai herdar toda a consulta do index la em cima
    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs



class PostDetalhes(UpdateView):
    pass

