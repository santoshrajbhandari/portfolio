from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    period = models.CharField(
        max_length=100,
        help_text="e.g. Jan 2023 – Present or 2021"
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']          # newest first
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.title} at {self.company}"


class Project(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField()
    link = models.URLField(blank=True, help_text="Optional project/demo URL")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
