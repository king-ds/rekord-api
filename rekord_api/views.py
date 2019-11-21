# Django
from django.shortcuts import render
from django.http import HttpResponse

# Django Rest
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Application
from rekord_api.serializers import TransportationSerializer, TransportationUpdateSerializer
from rekord_api.models import Transportation

def test(request):
    return HttpResponse("Hello World")

class CreateTransportation(generics.CreateAPIView):
    model = Transportation
    serializer_class = TransportationSerializer

class ListTransportation(generics.ListAPIView):
    queryset = Transportation.objects.filter(arrived = False)
    serializer_class = TransportationSerializer

class UpdateTransportation(generics.UpdateAPIView):
    serializer_class = TransportationUpdateSerializer
    lookup_field = 'id'
    queryset = Transportation.objects.all()