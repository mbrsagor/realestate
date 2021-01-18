from rest_framework.serializers import ModelSerializer

from .models import Lead


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
