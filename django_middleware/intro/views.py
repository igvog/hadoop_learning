from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def showtime(request):
    raise Exception('Django middleware')
    # return HttpResponse('Request time is: {}'.format(request.current_time))
