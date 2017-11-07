from django.db import models

# Create your models here.

class Farms(models.Model):

    class Meta:

        db_table = 'farms'
        verbose_name = 'farm'
        verbose_name_plural = 'farms'

    id = models.UUIDField(primary_key=True, unique=True, editable=True)
    code = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    active = models.BooleanField()



