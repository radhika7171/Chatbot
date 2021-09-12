from django.db import models

# Create your models here


class CreateAppointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class CreateFutureAppointment(models.Model):
    Appointment_method = (
        ('A', 'Audio Call Appointment'),
        ('V', 'Video Confrence Appointment'),
        ('P', 'In-Person Physical Appointment'),
    )

    preffered_day = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thur', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturay'),
    )
    # appappointment_method_choices = models.CharField(max_length=60)
    appointment_method_choice = models.CharField(
        max_length=20, choices=Appointment_method)

    preferred_day_choice = models.CharField(
        max_length=20, choices=preffered_day)

    def is_choice_appointment_method(self):
        return self.appointment_method_choice

    def is_choice_preffered_day(self):
        return self.preferred_day_choice
