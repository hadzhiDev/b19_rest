from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Apartment, Object, Block
from .serializers import ApartmentModelSerializer


# @api_view(['GET'])
# def apartments_list(request):
#     apartments = Apartment.objects.all()
#     serializer = ApartmentSerializer(apartments, many=True) 
#     return Response(serializer.data)


class ApartmentListCreateView(ListCreateAPIView):
    serializer_class = ApartmentModelSerializer
    queryset = Apartment.objects.all()


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApartmentModelSerializer
    queryset = Apartment.objects.all()