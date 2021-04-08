from leads.models.lead import Lead
from rest_framework.serializers import ModelSerializer


class LeadSerializer(ModelSerializer):
    
    class Meta:
        model = Lead
        fields = '__all__'
