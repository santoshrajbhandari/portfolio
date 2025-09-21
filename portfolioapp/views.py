from django.shortcuts import render
from .models import Experience, Project,Skill
# Create your views here.
def home(request):
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'index.html', {
            "experiences": experiences,
            "projects": projects,
            "skills": skills,
        },)