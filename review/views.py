from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CommentModel
from bookings.models import BookingModel
from .serializers import CommentModelSerializer

class CommentList(APIView):

    def get(self, request, format=None):
        comments = CommentModel.objects.all()
        serializer = CommentModelSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        campaign_id = request.data.get('campaign')
        patient = request.user

        if not BookingModel.objects.filter(campaign_id=campaign_id, patient=patient).exists():
            return Response({'error': 'You cannot leave a comment without booking a service for this campaign.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return CommentModel.objects.get(pk=pk)
        except CommentModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)