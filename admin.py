from django.contrib import admin
from .models import Subject, Attendance, TeacherProfile


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the 'name' field in the admin list view


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'date', 'is_present')
    list_filter = ('is_present',)
    search_fields = ('subject__name', 'teacher__username')  # Enable search by subject name or teacher username


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Display the 'user' field in the admin list view
