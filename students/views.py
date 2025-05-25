from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Student, Course, Grade, UserActivity
from .forms import StudentForm, CourseForm, GradeForm
from django.contrib.auth import login, authenticate
from django.utils import timezone

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Record login activity
            UserActivity.objects.create(
                user=user,
                action='login',
                details=f'User {user.username} logged in',
                timestamp=timezone.now()
            )
            next_url = request.POST.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'students/login.html')

@login_required
def home(request):
    context = {
        'students_count': Student.objects.count(),
        'courses_count': Course.objects.count(),
        'grades_count': Grade.objects.count(),
        'activities_count': UserActivity.objects.count(),
        'recent_activities': UserActivity.objects.all()[:10]
    }
    return render(request, 'students/home.html', context)

@login_required
def student_list(request):
    students = Student.objects.all().order_by('last_name')
    UserActivity.objects.create(
        user=request.user,
        action='view_student',
        details='Viewed student list'
    )
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    grades = Grade.objects.filter(student=student)
    UserActivity.objects.create(
        user=request.user,
        action='view_student',
        details=f'Viewed details for student: {student.first_name} {student.last_name}'
    )
    return render(request, 'students/student_detail.html', {
        'student': student,
        'grades': grades
    })

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            UserActivity.objects.create(
                user=request.user,
                action='view_student',
                details=f'Created new student: {student.first_name} {student.last_name}'
            )
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            UserActivity.objects.create(
                user=request.user,
                action='edit_student',
                details=f'Edited student: {student.first_name} {student.last_name}'
            )
            messages.success(request, 'Student updated successfully!')
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_name = f'{student.first_name} {student.last_name}'
        student.delete()
        UserActivity.objects.create(
            user=request.user,
            action='delete_student',
            details=f'Deleted student: {student_name}'
        )
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

@login_required
def course_list(request):
    courses = Course.objects.all().order_by('course_code')
    UserActivity.objects.create(
        user=request.user,
        action='view_course',
        details='Viewed course list'
    )
    return render(request, 'students/course_list.html', {'courses': courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    grades = Grade.objects.filter(course=course)
    UserActivity.objects.create(
        user=request.user,
        action='view_course',
        details=f'Viewed details for course: {course.course_code}'
    )
    return render(request, 'students/course_detail.html', {
        'course': course,
        'grades': grades
    })

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            UserActivity.objects.create(
                user=request.user,
                action='view_course',
                details=f'Created new course: {course.course_code}'
            )
            messages.success(request, 'Course created successfully!')
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'students/course_form.html', {'form': form})

@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            UserActivity.objects.create(
                user=request.user,
                action='edit_course',
                details=f'Edited course: {course.course_code}'
            )
            messages.success(request, 'Course updated successfully!')
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/course_form.html', {'form': form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course_code = course.course_code
        course.delete()
        UserActivity.objects.create(
            user=request.user,
            action='delete_course',
            details=f'Deleted course: {course_code}'
        )
        messages.success(request, 'Course deleted successfully!')
        return redirect('course_list')
    return render(request, 'students/course_confirm_delete.html', {'course': course})

@login_required
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save()
            UserActivity.objects.create(
                user=request.user,
                action='record_grade',
                details=f'Recorded grade for {grade.student} in {grade.course}'
            )
            messages.success(request, 'Grade recorded successfully!')
            return redirect('student_list')
    else:
        initial = {}
        course_id = request.GET.get('course')
        if course_id:
            try:
                course = Course.objects.get(pk=course_id)
                initial['course'] = course
            except Course.DoesNotExist:
                pass
        form = GradeForm(initial=initial)
    return render(request, 'students/grade_form.html', {'form': form}) 