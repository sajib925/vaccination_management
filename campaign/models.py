from django.db import models

class CampaignModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class VaccinesModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ScheduleModel(models.Model):
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(VaccinesModel, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.campaign.name} - {self.vaccine.name} on {self.date}"