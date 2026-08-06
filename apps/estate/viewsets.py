from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions

from .models import Apartment, Object, Block
from .serializers import ApartmentModelSerializer, BlockModelSerializer, ObjectModelSerializer
from api.paginations import SimplePagePagination


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentModelSerializer
    queryset = Apartment.objects.all()
    pagination_class = SimplePagePagination
    permission_classes = (permissions.AllowAny,)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class ObjectViewSet(ModelViewSet):
    serializer_class = ObjectModelSerializer
    queryset = Object.objects.all()
    pagination_class = SimplePagePagination
    permission_classes = (permissions.AllowAny,)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class BlockViewSet(ModelViewSet):
    serializer_class = BlockModelSerializer
    queryset = Block.objects.all()
    pagination_class = SimplePagePagination
    permission_classes = (permissions.AllowAny,)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
