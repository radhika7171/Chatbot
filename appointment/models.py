from django.db import models

# Create your models here.


class CreateAppointment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=255, unique=False, null=False)
    last_name = models.CharField(max_length=255, unique=False, null=False)
