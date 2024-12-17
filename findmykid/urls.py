from django.urls import path
from .views import Base, Report
from . import views

urlpatterns = [
    path('base/', Base.as_view(), name='base'),
    path('report/', views.report, name='report'),

]