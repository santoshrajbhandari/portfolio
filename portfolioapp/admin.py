from django.contrib import admin
from .models import Experience, Project, Skill
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "period")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    
admin.site.register(Skill)