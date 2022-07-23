from django import views
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super_Types
from .serializers import Super_types_serializers
from supers import serializers

@api_view(['GET', 'POST'])
def Super_type_list(request):
   
   
    if request.method == 'GET':
        super_type = Super_Types.objects.all()
        serializer = Super_types_serializers(super_type, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Super_types_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
            
@api_view(['GET', 'PUT', 'DELETE'])
def Super_type_detail(request, pk):
    product = get_object_or_404(Super_Types, pk=pk)
    if request.method == 'GET':
        serializer = Super_types_serializers(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Super_types_serializers(product, data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
