from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Attendance
from .forms import AttendanceForm, SubjectForm



def my_protected_view(request):
    # Your view logic here
    return render(request, 'welcome.html')




@login_required

def mark_attendance_view(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance_instance = form.save(commit=False)
            attendance_instance.subject = subject
            attendance_instance.teacher = request.user
            attendance_instance.save()

            # Redirect to view_attendance after successful form submission
            return redirect('view_attendance', subject_id=subject_id)
    else:
        form = AttendanceForm()

    return render(request, 'mark_attendance.html', {'form': form, 'subject': subject})



def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()

    return render(request, 'create_subject.html', {'form': form})



def view_attendance(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    attendance_records = Attendance.objects.filter(subject=subject)

    return render(request, 'view_attendance.html', {'subject': subject, 'attendance_records': attendance_records})

def subject_list(request):
    subjects = Subject.objects.all()  # Fetch all subjects from the database
    return render(request, 'subject_list.html', {'subjects': subjects})


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    if request.method == 'POST':
        # Delete the subject
        subject.delete()
        return redirect('subject_list')  # Redirect to a subject list or another page after deletion

    return render(request, 'confirm_subject_delete.html', {'subject': subject})




def confirm_subject_delete(request, pk):
    # Your view logic for confirming subject deletion
    subject = Subject.objects.get(pk=pk)
    context = {
        'subject': subject # Pass the subject to the template
        # Add other data you might need in the confirmation template
        # Example: 'confirmation_message': 'Are you sure you want to delete this subject?'
    }
    return render(request, 'confirm_subject_delete.html', context)
