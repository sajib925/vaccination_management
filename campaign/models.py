from django.conf import settings
from django.db import models

class CampaignModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class VaccinesModel(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=20)
    schedule = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

