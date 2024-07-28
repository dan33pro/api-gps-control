from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Interested
from .serializer import InterestedSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


@extend_schema(
    methods=['GET'],
    responses={200: InterestedSerializer(many=True)}
)
@extend_schema(
    methods=['POST'],
    request=InterestedSerializer,
    responses={201: InterestedSerializer, 400: 'Bad Request'}
)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def interested_list_create(request):
    if request.method == 'GET':
        interesteds = Interested.objects.all()
        serializer = InterestedSerializer(interesteds, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InterestedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    methods=['GET'],
    responses={200: InterestedSerializer}
)
@extend_schema(
    methods=['PUT'],
    request=InterestedSerializer,
    responses={200: InterestedSerializer, 400: 'Bad Request'}
)
@extend_schema(
    methods=['PATCH'],
    request=InterestedSerializer,
    responses={200: InterestedSerializer, 400: 'Bad Request'}
)
@extend_schema(
    methods=['DELETE'],
    responses={204: None}
)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])
def interested_detail(request, pk):
    interested = get_object_or_404(Interested, pk=pk)

    if request.method == 'GET':
        serializer = InterestedSerializer(interested)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InterestedSerializer(interested, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = InterestedSerializer(
            interested, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        interested.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
