from django.contrib import admin
from .models import Student, Course, Grade, UserActivity

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'email', 'enrollment_date')
    search_fields = ('student_id', 'first_name', 'last_name', 'email')
    list_filter = ('enrollment_date',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'credits', 'instructor')
    search_fields = ('course_code', 'course_name', 'instructor')
    list_filter = ('credits',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'semester', 'date_recorded')
    search_fields = ('student__first_name', 'student__last_name', 'course__course_code')
    list_filter = ('semester', 'date_recorded')

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'details')
    search_fields = ('user__username', 'action', 'details')
    list_filter = ('action', 'timestamp')
    readonly_fields = ('user', 'action', 'timestamp', 'details') 