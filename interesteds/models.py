from django.db import models

class Interested(models.Model):
    id_interested = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    applicant = models.CharField(max_length=100)