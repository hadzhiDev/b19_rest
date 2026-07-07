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


@api_view(['POST'])
def apartment_create(request):
    serializer = ApartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET"])
def apartment_detail(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    serializer = ApartmentSerializer(apartment)
    return Response(serializer.data)


@api_view(["PUT"])
def apartment_put(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    serializer = ApartmentSerializer(data=request.data, instance=apartment)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,)
    return Response(serializer.errors)


@api_view(["DELETE"])
def apartment_delete(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    apartment.delete()
    return Response({"message": "No content"})


# @api_view(['GET'])
# def objects_list(request):
#     objects = Object.objects.all()
    # serializer