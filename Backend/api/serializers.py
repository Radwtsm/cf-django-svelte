from rest_framework.serializers import ModelSerializer
from .models import DatiPersona


class DatiPersonaSerializer(ModelSerializer):
    class Meta:
        model = DatiPersona
        fields = '__all__'
