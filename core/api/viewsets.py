from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter, )
    # permission_classes = (DjangoModelPermissions, )
    # authentication_classes = (TokenAuthentication, )
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    #lookup_field = 'nome' #para mudar o identificador de busca que é id

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)

        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset
