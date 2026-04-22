from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nome')
    serializer_class = AutorSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(nacionalidade__icontains=q))
        return qs

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.livros.exists():
            return Response(
                {'detail': 'Não é possível excluir este autor pois ele possui livros cadastrados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(instance)
        return Response({'detail': f'Autor "{instance.nome}" excluído com sucesso.'}, status=status.HTTP_200_OK)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(nome__icontains=q)
        return qs

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': f'Categoria "{instance.nome}" excluída com sucesso.'}, status=status.HTTP_200_OK)


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.select_related('autor', 'categoria').all()
    serializer_class = LivroSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        status_filter = self.request.query_params.get('status')
        categoria = self.request.query_params.get('categoria')
        autor = self.request.query_params.get('autor')

        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(autor__nome__icontains=q) | Q(isbn__icontains=q))
        if status_filter:
            qs = qs.filter(status=status_filter)
        if categoria:
            qs = qs.filter(categoria_id=categoria)
        if autor:
            qs = qs.filter(autor_id=autor)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        livro = serializer.save()
        return Response(
            {'detail': f'Livro "{livro.titulo}" cadastrado com sucesso.', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        livro = serializer.save()
        return Response(
            {'detail': f'Livro "{livro.titulo}" atualizado com sucesso.', 'data': serializer.data}
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        titulo = instance.titulo
        self.perform_destroy(instance)
        return Response({'detail': f'Livro "{titulo}" excluído com sucesso.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='por-status')
    def por_status(self, request):
        data = {}
        for key, label in Livro.STATUS_CHOICES:
            data[key] = {'label': label, 'total': Livro.objects.filter(status=key).count()}
        return Response(data)
