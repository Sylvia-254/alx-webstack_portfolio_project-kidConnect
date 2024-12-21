from django.shortcuts import render
from django.views.generic import TemplateView

#import models here
from .models import Report

# Create your views here.
# def base(request):
#     """rendering the base file for testing purposes"""
#     return render(request, 'base.html')

class Base(TemplateView):
    template_name = 'base.html'

# class Report(TemplateView):
#     template_name = 'report.html'

def report(request):
    """the report page and its logic is here"""
    if request.method == 'POST':
        firstName = request.POST['firstName']
        middleName = request.POST['middleName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        height = request.POST['height']
        skinTone = request.POST['skinTone']
        location = request.POST['location']
        dressing = request.POST['dressing']
        profilePhoto = request.POST['profilePhoto']
        status = request.POST['status']
        #mapping each entry in a new report
        newReport = Report(firstName=firstName, middleName=middleName, lastName=lastName, email=email,\
                           gender=gender, age=age, height=height, skinTone=skinTone, location=location, dressing=dressing,\
                            profilePhoto=profilePhoto, status = status)
        
        newReport.save()
    return render(request, 'report.html')

def reported(request):
    """logic for retrieving reported children from the database"""
    context = {}
    reportedChildren = Report.objects.all()
    context['reportedChildren'] =  reportedChildren
    return render(request, 'reportedChildren.html', context)

# reportedChildren search
def search(request):
    """logic for the search bar and button"""
    if request.method == 'GET':
        search = request.GET['search']
        posts = Report.objects.filter(firstName = search) | Report.objects.filter(middleName = search) | Report.objects.filter(lastName = search) 
        return render(request, 'search.html', {'posts':posts, 'search':search})