from django.urls import path
from .views import CampaignList, CampaignDetail, VaccineList, VaccineDetail, ScheduleList, ScheduleDetail

urlpatterns = [
    path("", CampaignList.as_view(), name="campaign_list"),
    path("", ScheduleList.as_view(), name="schedule_list"),
    path("vaccines/", VaccineList.as_view(), name="vaccine_list"),
    path("<int:pk>/", CampaignDetail.as_view(), name="campaign_detail"),
    path("<int:pk>/", ScheduleDetail.as_view(), name="schedule_detail"),
    path("<int:pk>/", VaccineDetail.as_view(), name="vaccine_detail"),
]
