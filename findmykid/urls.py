from django.urls import path
from .views import Base, Report

urlpatterns = [
    path('base/', Base.as_view(), name='base'),
    path('report/', Report.as_view(), name='report'),

]