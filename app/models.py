from django.contrib.gis.db import models #because we are using gis db

class Myplaces(models.Model):
    name = models.CharField(max_length=100) #name of your place
    location = models.PointField()

    def __str__(self):
        return self.name