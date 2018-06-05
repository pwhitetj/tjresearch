from django.forms import ModelForm
from .models import ResearchLab, Student, Project
from django.forms.models import inlineformset_factory


class ResearchLabForm(ModelForm):
    class Meta:
        model = ResearchLab
        fields = ['lab_name', 'lab_description']


StudentsFormSet = inlineformset_factory(Student, Project)