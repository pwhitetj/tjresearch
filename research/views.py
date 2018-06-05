from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "research/index.html")

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Student, Project, ResearchLab


class ProjectIndexView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

class StudentIndexView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class ProjectCreateView(generic.CreateView):
    model = Project
    fields = ['title', 'abstract', 'paper', 'director']
    success_url = '/research/projects/'

class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = ['title', 'abstract', 'paper', 'director']
    success_url = '/research/projects/'

class ProjectDeleteView(generic.DeleteView):
    model = Project
    fields = ['title', 'abstract', 'paper', 'director']
    success_url = '/research/projects/'

class ResearchLabIndexView(generic.ListView):
    model = ResearchLab

class ResearchLabCreate(generic.CreateView):
    model = ResearchLab
    fields = ['lab_name', 'lab_description']
    success_url = '/research/research_labs/'

class ResearchLabUpdate(generic.UpdateView):
    model = ResearchLab
    fields = ['lab_name', 'lab_description']
    success_url = '/research/research_labs/'


class ResearchLabDelete(generic.DeleteView):
    model = ResearchLab
    fields = ['lab_name', 'lab_description']
    success_url = '/research/research_labs/'

