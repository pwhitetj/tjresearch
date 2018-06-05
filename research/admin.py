from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Project)
admin.site.register(ResearchLab)
admin.site.register(LabDirector)