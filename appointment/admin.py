from django.contrib import admin
from django.db import models
from .models import CreateAppointment, CreateFutureAppointment

admin.site.register(CreateAppointment)
admin.site.register(CreateFutureAppointment)

# Register your models here.


class CreateAppointmentAdmin(admin.ModelAdmin):

    list_display = ("id", "first_name", "last_name", "phone",
                    "email", "city", "state", "country")

    first_name = models.CharField(max_length=50)

    def first_name(self):
        return self.first_name


class CreateFutureAppointmentAdmin(admin.ModelAdmin):
    list_display_1 = ("id", "Appointment_method")
    list_display_2 = ("id", "preferred_day_choice")
