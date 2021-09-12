from django.contrib import admin
from .models import CreateAppointment, CreateFutureAppointment

admin.site.register(CreateAppointment)
admin.site.register(CreateFutureAppointment)

# Register your models here.


class CreateAppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone",
                    "email", "city", "state", "country")


class CreateFutureAppointmentAdmin(admin.ModelAdmin):
    list_display_1 = ("id", "Appointment_method")
    list_display_2 = ("id", "preferred_day_choice")
