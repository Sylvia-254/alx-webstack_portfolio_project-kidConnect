from django.urls import path
from .views import Base, Report, IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('register/', views.registerPage, name="register"),
    path('base/', Base.as_view(), name='base'),
    path('report/', views.report, name='report'),
    path('reported/', views.reported, name='reportedChildren'),
    path('search/', views.search, name="search"),

]