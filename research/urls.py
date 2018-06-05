from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^[/]*$', views.index, name='index'),
    url(r'^students/$', views.StudentIndexView.as_view(), name='student'),
    url(r'^projects/$', views.ProjectIndexView.as_view(), name='project'),
    url(r'^projects/add$', views.ProjectCreateView.as_view(), name='project_add'),
    url(r'^projects/update/(?P<pk>[0-9]+)$', views.ProjectUpdateView.as_view(), name='project_update'),
    url(r'^projects/delete/(?P<pk>[0-9]+)$', views.ProjectDeleteView.as_view(), name='project_delete'),
    url(r'^research_labs/$', views.ResearchLabIndexView.as_view(), name='researchlab'),
    url(r'^project_detail/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^student_detail/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='student_detail'),
    url(r'^research_lab/add/$', views.ResearchLabCreate.as_view(), name='research_lab_add'),
    url(r'^research_lab/update/(?P<pk>[0-9]+)/$', views.ResearchLabUpdate.as_view(), name='research_lab_update'),
    url(r'^research_lab/delete/(?P<pk>[0-9]+)/$', views.ResearchLabDelete.as_view(), name='research_lab_delete'),

]

