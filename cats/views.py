from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serealizes import CatSerializer, OwnerSerializer
from .models import Cat, Owner
from rest_framework.views import APIView


# @api_view(['POST', 'GET'])
# def cat_list(request):
#     if request.method == 'POST':
#         serealizer = CatSerializer(data=request.data, many=True)
#         if serealizer.is_valid():
#             serealizer.save()
#             return Response(data=serealizer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serealizer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cat = Cat.objects.all().order_by('-id')
#     serealizer = CatSerializer(cat, many=True)
#     return Response(data=serealizer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['PATCH', 'GET', 'PUT', 'DELETE'])
# def cat_detail(request, pk):
#     cat = Cat.objects.get(pk=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serealizer = CatSerializer(instance=cat, data=request.data, partial=True)
#         if serealizer.is_valid():
#             serealizer.save()
#             return Response(serealizer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serealizer = CatSerializer(instance=cat)
#     return Response(data=serealizer.data, status=status.HTTP_200_OK)
#
#
# class CatListAPI(APIView):
#     def get(self, request):
#         cat = Cat.objects.all().order_by('-id')
#         serealizer = CatSerializer(cat, emany=True)
#         return Response(data=serealizer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer