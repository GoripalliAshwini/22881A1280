from django.db import models
from django.utils import timezone
from datetime import timedelta

class ShortURL(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    validity = models.IntegerField(default=30)  
    clicks = models.IntegerField(default=0) 
    @property
    def expiry(self):
        return self.created_at + timedelta(minutes=self.validity)



