from appointment.models import CreateAppointment
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# @csrf_exempt
def create_new_appointment(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # Saving to the database
        new_appointment = CreateAppointment(1, first_name, last_name)
        new_appointment.save()

    context = {}
    return render(request, 'create_appointment.html', context)


def chatbot_index(request):
    return render(request, 'chatbot_index.html', {})
