from django.urls import path
from . import views

app_name = 'labs'

urlpatterns = [
    path('', views.main, name='main')
]