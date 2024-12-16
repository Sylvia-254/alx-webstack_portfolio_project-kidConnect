from django.shortcuts import render

# Create your views here.
def base(request):
    """rendering the base file for testing purposes"""
    return render(request, 'base.html')