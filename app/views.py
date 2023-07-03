from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from django.shortcuts import render

from .models import Employee


# Create your views here.


class EmpView(ListView):
    model = Employee
    template_name = 'emp.html'
    context_object_name = 'emp'


class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('employee')


class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('login')  # Redirect to the login page after logout

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class CreateEmp(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['employee_name', 'photo', 'designation','qualification','address','remarks','salary','Status','phone','email']
    success_url = reverse_lazy('employee')
    template_name = 'create_emp.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEmp, self).form_valid(form)

class Details(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'details.html'

class Delete(LoginRequiredMixin, DeleteView):
    model = Employee
    fields = ['__all__']
    success_url = reverse_lazy('employee')
    template_name = 'delete.html'

class Update(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['photo','designation','qualification','address','remarks','salary','phone','email','Status']
    success_url = reverse_lazy('employee')
    template_name = 'create_emp.html'





