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
        serializer = BookingModelSerializer(data=request.data)
        serializer.patient = request.user
        if serializer.is_valid():
            serializer.save(patient = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(APIView):

    def get_object(self, pk):
        try:
            return BookingModel.objects.get(pk=pk)
        except BookingModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingModelSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingModelSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
