from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import School, Student
from .forms import SchoolForm, StudentForm


class SchoolListView(ListView):
    model = School
    template_name = 'items/school_list.html'
    context_object_name = 'schools'


class SchoolCreateView(CreateView):
    model = School
    form_class = SchoolForm
    template_name = 'items/school_form.html'
    success_url = reverse_lazy('school-list')


class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = 'items/school_form.html'
    success_url = reverse_lazy('school-list')


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'items/school_confirm_delete.html'
    success_url = reverse_lazy('school-list')


class StudentListView(ListView):
    model = Student
    template_name = 'items/student_list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'items/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'items/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'items/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
