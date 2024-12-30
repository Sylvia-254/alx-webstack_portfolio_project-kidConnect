from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#import models here
from .models import Report

# Create your views here.
# def base(request):
#     """rendering the base file for testing purposes"""
#     return render(request, 'base.html')
class IndexView(TemplateView):
    template_name = 'index.html'

def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        # checking if username exists
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")
        # checking if the email exists
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")
        #checking the password length
        if len(password) < 5:
            messages.error(request, "Password must be atleast 5 characters")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            messages.success(request, "Account created successfully, login now")
            #return rediret('login')
    return render(request, 'register.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

class Base(TemplateView):
    template_name = 'base1.html'


def logoutView(request):
    logout(request)
    return redirect('home')
# class Report(TemplateView):
#     template_name = 'report.html'
@login_required # restrict this page to authenticated users
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

@login_required #restrict this page to authenticated users
def reported(request):
    """logic for retrieving reported children from the database"""
    context = {}
    reportedChildren = Report.objects.all()
    context['reportedChildren'] =  reportedChildren
    return render(request, 'reportedChildren.html', context)

# reportedChildren search
@login_required #restrict this page to restricted users
def search(request):
    """logic for the search bar and button"""
    if request.method == 'GET':
        search = request.GET['search']
        posts = Report.objects.filter(firstName = search) | Report.objects.filter(middleName = search) | Report.objects.filter(lastName = search) 
        return render(request, 'search.html', {'posts':posts, 'search':search})


#customAdmin view
def customAdmin(request):
    reportedChildren = Report.objects.all()
    context = {'reportedChildren' : reportedChildren }
    return render(request, 'customAdmin.html', context)

#admin update button
def updateDetails(request, id): 
    updateChild = get_object_or_404(Report, id=id)
    reportedChildImage = updateChild.profilePhoto.url
    if request.method == 'POST':
        updateChild.firstName = request.POST.get('firstName')
        updateChild.middleName = request.POST.get('middleName')
        updateChild.lastName = request.POST.get('lastName')
        updateChild.email = request.POST.get('email')
        updateChild.gender = request.POST.get('gender')
        updateChild.age = request.POST.get('age')
        updateChild.height = request.POST.get('height')
        updateChild.skinTone = request.POST.get('skinTone')
        updateChild.location = request.POST.get('location')
        updateChild.dressing = request.POST.get('dressing')
        new_profile_photo = request.FILES.get('profilePhoto')  # Use FILES for image uploads

        if new_profile_photo:
            # If a new image is uploaded, update the field
            updateChild.profilePhoto = new_profile_photo
        else:
            # If no new image is provided, keep the existing image
            # This line isn't necessary unless you overwrite the field elsewhere
            pass
        updateChild.status = request.POST.get('status')
        updateChild.save()
    context = { 'updateChild':updateChild, 'reportedChildImage':reportedChildImage }
    return render(request, 'update.html', context)

# customAdmin/delete
def delete(request, id):
    deleteChild = Report.objects.get(id=id)
    deleteChild.delete()
    return redirect('customAdmin')

#generateDetails
def generateDetails(request, id):
    """logic and back end for the generate Details button in reported page"""
    reportedChild = Report.objects.get(id=id)
    email = reportedChild.email
    context = {'reportedChild':reportedChild, 'email':email }

    return render(request, 'generateDetails.html', context)

