from django.db import models
from django.contrib.auth.models import User


class Urls(models.Model):
    oirignal_url=models.URLField(blank=False,max_length=250);
    short_query=models.URLField(blank=False,max_length=25);
    visit=models.IntegerField(default=0);
    user=models.ForeignKey(User,on_delete=models.CASCADE)
