from rest_framework import viewsets
from .serializer import InterestedSerializer
from .models import Interested

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = Interested.objects.all()
    serializer_class = InterestedSerializer