# attendee/attendance_app/urls.py

from django.urls import path
from . import views, admin
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('welcome/', views.my_protected_view, name='welcome_page'),

    path('subjects/', views.subject_list, name='subject_list'),
    path('mark_attendance/<int:subject_id>/', views.mark_attendance_view, name='mark_attendance'),

    path('create_subject/', views.create_subject, name='create_subject'),
    path('view_attendance/<int:subject_id>/', views.view_attendance, name='view_attendance'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('confirm_delete/<int:pk>/', views.confirm_subject_delete, name='confirm_subject_delete')

    # Add other URLs as needed for updating/deleting subjects, etc.
]
