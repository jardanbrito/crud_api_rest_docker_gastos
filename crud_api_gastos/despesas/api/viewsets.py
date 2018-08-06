from rest_framework.viewsets import ModelViewSet
from despesas.models import Despesas
from .serializers import DespesasSerializer


class DespesasViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer