from django.db import models
from django.contrib.auth.models import User


# Model representing Subjects
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model representing Attendance records
class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)


# Model representing Teachers
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

