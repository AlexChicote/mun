from django.db import models
from django.contrib.auth.models import User

class Integration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=256, null=True)
    integration_user_id = models.CharField(max_length=256, null=True)

class Artist(models.Model):
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE)
    integration_artist_id = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256)
