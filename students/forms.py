from django import forms
from .models import Student, Course, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 
                 'date_of_birth', 'address', 'phone_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'description', 
                 'credits', 'instructor']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade', 'semester']
        widgets = {
            'grade': forms.NumberInput(attrs={'min': 0, 'max': 100, 'step': 0.01}),
        } 