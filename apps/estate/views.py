from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Apartment, Object, Block
from .serializers import ApartmentSerializer


@api_view(['GET'])
def apartments_list(request):
    apartments = Apartment.objects.all()
    serializer = ApartmentSerializer(apartments, many=True) 
    return Response(serializer.data)


@api_view(['GET'])
def objects_list(request):
    objects = Object.objects.all()
    # serializer