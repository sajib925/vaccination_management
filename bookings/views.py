from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookingModel
from .serializers import BookingModelSerializer

class BookingList(APIView):
    def get(self, request, format=None):
        bookings = BookingModel.objects.all()
        serializer = BookingModelSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        if request.user.user_type != 'patient':
            return Response({"detail": "Only patients can make bookings."}, status=status.HTTP_403_FORBIDDEN)

        serializer = BookingModelSerializer(data=request.data)
        serializer.patient = request.user
        if serializer.is_valid():
            serializer.save(patient = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

