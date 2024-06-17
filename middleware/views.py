# myapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .soap_client import call_b2c_service
from .serializers import B2CRequestSerializer


# Zamtel API Request Function


@api_view(['POST'])
def b2c_request_view(request):
    serializer = B2CRequestSerializer(data=request.data)
    if serializer.is_valid():
        response = call_b2c_service(serializer.validated_data)
        return Response({'response': response}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
