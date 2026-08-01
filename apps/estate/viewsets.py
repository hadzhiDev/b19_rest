from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Apartment, Object, Block
from .serializers import ApartmentModelSerializer, BlockModelSerializer, ObjectModelSerializer
from api.paginations import SimplePagePagination


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentModelSerializer
    queryset = Apartment.objects.all()
    pagination_class = SimplePagePagination
