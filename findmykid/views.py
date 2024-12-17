from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def base(request):
#     """rendering the base file for testing purposes"""
#     return render(request, 'base.html')

class Base(TemplateView):
    template_name = 'base.html'

class Report(TemplateView):
    teplate_name = 'report.html'