from appointment.models import CreateAppointment, CreateFutureAppointment
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# @csrf_exempt
def create_new_appointment(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')

        # Saving to the database
        new_appointment = CreateAppointment(
            1, first_name, last_name, phone, email, city, state, country)
        new_appointment.save()

    context = {}
    return render(request, 'create_appointment.html', context)


def create_second_appointment(request):
    if request.method == 'POST':
        appointment_method = request.POST.get('appointment_method')
        preferred_day = request.POST.get('day')

        # saving to database
        second_appointment = CreateFutureAppointment(
            1, appointment_method, preferred_day)
        second_appointment.save()

    context = {}
    return render(request, 'second_appointment.html', context)


def chatbot_index(request):
    return render(request, 'chatbot_index.html', {})
