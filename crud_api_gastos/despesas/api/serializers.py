from rest_framework.serializers import ModelSerializer
from despesas.models import Despesas

class DespesasSerializer(ModelSerializer):
    class Meta:
        model = Despesas
        fields = ('id', 'descricao', 'data', 'valor', 'comentario')