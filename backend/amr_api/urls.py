from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('options/', views.options, name='options'),
    path('summary/counts-summary', views.counts_summary, name='counts_summary'),
    path('summary/time-trends', views.time_trends, name='time_trends'),
    path('summary/antibiogram', views.antibiogram, name='antibiogram'),
    path('summary/sex-age', views.sex_age, name='sex_age'),
    path('geo/facilities', views.facilities, name='facilities'),
]
