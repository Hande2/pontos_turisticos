from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSet(ModelViewSet):

    #queryset = PontosTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome =  self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontosTuristico.objects.all()

        if id:
            queryset = PontosTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexac=nome)

        return queryset



    """def list(self, request, *args, **kwargs):
        return Response ({'teste':123})"""

    """def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass"""