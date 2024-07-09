from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CampaignModel, VaccinesModel, ScheduleModel
from .serializers import CampaignModelSerializer, VaccinesModelSerializer, ScheduleModelSerializer
from .permissions import IsDoctor
from rest_framework.permissions import IsAuthenticated

class CampaignList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        campaigns = CampaignModel.objects.all()
        serializer = CampaignModelSerializer(campaigns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.check_permissions(request)  # Check if user has permission to post
        serializer = CampaignModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CampaignModel.objects.get(pk=pk)
        except CampaignModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        campaign = self.get_object(pk)
        serializer = CampaignModelSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to put
        campaign = self.get_object(pk)
        serializer = CampaignModelSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to delete
        campaign = self.get_object(pk)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VaccineList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        vaccines = VaccinesModel.objects.all()
        serializer = VaccinesModelSerializer(vaccines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.check_permissions(request)  # Check if user has permission to post
        serializer = VaccinesModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VaccineDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return VaccinesModel.objects.get(pk=pk)
        except VaccinesModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vaccine = self.get_object(pk)
        serializer = VaccinesModelSerializer(vaccine)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to put
        vaccine = self.get_object(pk)
        serializer = VaccinesModelSerializer(vaccine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to delete
        vaccine = self.get_object(pk)
        vaccine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ScheduleList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        schedules = ScheduleModel.objects.all()
        serializer = ScheduleModelSerializer(schedules, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.check_permissions(request)  # Check if user has permission to post
        serializer = ScheduleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScheduleDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ScheduleModel.objects.get(pk=pk)
        except ScheduleModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        schedule = self.get_object(pk)
        serializer = ScheduleModelSerializer(schedule)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to put
        schedule = self.get_object(pk)
        serializer = ScheduleModelSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.check_permissions(request)  # Check if user has permission to delete
        schedule = self.get_object(pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
