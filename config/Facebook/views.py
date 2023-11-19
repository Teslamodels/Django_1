from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def HomePageView(request):
    return HttpResponse("I'm here to change the worls!")

class Billioneries(TemplateView):
    template_name = 'index.html'
