from django.urls import path
from .views import Base, Report
from . import views

urlpatterns = [
    path('', )
    path('base/', Base.as_view(), name='base'),
    path('report/', views.report, name='report'),
    path('reported/', views.reported, name='reportedChildren'),
    path('search/', views.search, name="search"),

]