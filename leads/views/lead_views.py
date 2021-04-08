from leads.models.lead import Lead
from leads.serializers.lead_serializer import LeadSerializer
from rest_framework import permissions, viewsets


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.AllowAny]
