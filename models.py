from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employer = models.BooleanField(default=False, help_text="Designates whether this user can post jobs.")
    is_job_seeker = models.BooleanField(default=True, help_text="Designates whether this user is looking for jobs.")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True, help_text="Comma separated skills")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
