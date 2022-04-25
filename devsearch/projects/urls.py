from . import views
from django.urls import path


urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]
