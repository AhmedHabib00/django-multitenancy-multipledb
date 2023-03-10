from django.shortcuts import render
from django.views.generic import ListView

from .models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors_list.html'
