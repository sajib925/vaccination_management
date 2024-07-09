from django.contrib import admin
from .models import CampaignModel, ScheduleModel, VaccinesModel

# Register your models here.

admin.site.register(CampaignModel)
admin.site.register(ScheduleModel)
admin.site.register(VaccinesModel)