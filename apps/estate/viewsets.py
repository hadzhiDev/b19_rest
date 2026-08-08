from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Apartment, Object, Block
from .serializers import ApartmentModelSerializer, BlockModelSerializer, ObjectModelSerializer
from api.paginations import SimplePagePagination
from api.permissions import IsSuperUser


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentModelSerializer
    queryset = Apartment.objects.all()
    pagination_class = SimplePagePagination
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ("rooms_count", "type", "block")
    ordering_fields = ("number", "floor")
    search_fields = ("block__object__name",)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            return [permissions.IsAdminUser()]
        elif self.action == "delete":
            return [IsSuperUser()]
        return super().get_permissions()

    def get_queryset(self):
        qs = Apartment.objects.all()
        block__number = self.request.query_params.get("block__number")
        print(block__number)
        qs = qs.filter(block__number=block__number)
        return qs


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
