from django import views
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Supers
from .serializers import Superserilaizers
from super_types.serializers import Super_types_serializers

@api_view(['GET', 'POST'])
def Supers_list(request):
    if request.method == 'GET':
       
        super_type = request.query_params.get('super_type_lookup')
        queryset = Supers.objects.all()
       
        if super_type:
           queryset = queryset.filter(super_type__type = super_type)

        serializer = Superserilaizers(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Superserilaizers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
            
@api_view(['GET', 'PUT', 'DELETE'])
def Super_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = Superserilaizers(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Superserilaizers(super, data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
