from rest_framework import viewsets, permissions
from .serializer import InterestedSerializer
from .models import Interested

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = Interested.objects.all().order_by('id_interested')
    permission_classes = [permissions.AllowAny]
    serializer_class = InterestedSerializer