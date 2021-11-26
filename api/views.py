

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from api.models import Practice
from api.serializers import PracticeSerializer


class PracticeListCreateAPIView(ListCreateAPIView):
  queryset = Practice.objects.all()
  serializer_class = PracticeSerializer

class PracticeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    lookup_field = 'pk'
