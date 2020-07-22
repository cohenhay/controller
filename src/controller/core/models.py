from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

class Server(models.Model):

     hostname= models.CharField(max_length=120)
     ipadress= models.GenericIPAddressField()
     os= models.CharField(max_length=120)
 

     def __str__(self):
          return self.hostname

     @property
     def owner(self):
        return self.hostname

     def get_api_url(self, request=None):
        return api_reverse("api-core:post-rud", kwargs={'pk': self.pk}, request=request)