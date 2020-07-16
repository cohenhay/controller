from django.db import models

class Server(models.Model):

     hostname= models.CharField(max_length=120)
     ipadress= models.GenericIPAddressField()
     os= models.CharField(max_length=120)

     def __str__(self):
          return self.hostname
     

