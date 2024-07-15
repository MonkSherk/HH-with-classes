from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator

from main_APP.forms import VacancyUpdateForm, VacancyCreateForm, ResumeUpdateForm, ResumeCreateForm, VacancyFilterForm
from main_APP.models import Vacancy, Resume


# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Vacancy, Resume
from .forms import ResumeCreateForm, ResumeUpdateForm, VacancyCreateForm, VacancyUpdateForm

class StartPageView(View):
    def get(self, request):
        return render(request, 'main_APP/start_page.html', context={'user': request.user})

class VacancyListView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'main_APP/vacancy_list.html', {'vacancies': vacancies})

class VacancyDetailView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'main_APP/vacancy_detail.html', {'vacancy': vacancy})

class ResumeListView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, 'main_APP/resume_list.html', {'resumes': resumes})

class ResumeDetailView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        return render(request, 'main_APP/resume_detail.html', {'resume': resume})

class ResumeCreateView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request):
        form = ResumeCreateForm()
        return render(request, 'main_APP/resume_create.html', {'form': form})

    @method_decorator(login_required(login_url='login_page'))
    def post(self, request):
        form = ResumeCreateForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list')
        return render(request, 'main_APP/resume_create.html', {'form': form})

class ResumeUpdateView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        form = ResumeUpdateForm(instance=resume)
        return render(request, 'main_APP/resume_update.html', {'form': form})

    @method_decorator(login_required(login_url='login_page'))
    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        form = ResumeUpdateForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
        return render(request, 'main_APP/resume_update.html', {'form': form})

class ResumeDeleteView(View):
    @method_decorator(login_required(login_url='login_page'))
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        resume.delete()
        return redirect('resume_list')

class VacancyCreateView(View):
    @method_decorator(login_required(login_url='login_page'))
    @method_decorator(staff_member_required(login_url=''))
    def get(self, request):
        form = VacancyCreateForm()
        return render(request, 'main_APP/vacancy_create.html', {'form': form})

    @method_decorator(login_required(login_url='login_page'))
    @method_decorator(staff_member_required(login_url=''))
    def post(self, request):
        form = VacancyCreateForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.user = request.user
            vacancy.save()
            return redirect('vacancy_list')
        return render(request, 'main_APP/vacancy_create.html', {'form': form})

class VacancyUpdateView(View):
    @method_decorator(login_required(login_url='login_page'))
    @method_decorator(staff_member_required(login_url=''))
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = VacancyUpdateForm(instance=vacancy)
        return render(request, 'main_APP/vacancy_update.html', {'form': form})

    @method_decorator(login_required(login_url='login_page'))
    @method_decorator(staff_member_required(login_url=''))
    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = VacancyUpdateForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
        return render(request, 'main_APP/vacancy_update.html', {'form': form})

class VacancyDeleteView(View):
    @method_decorator(login_required(login_url='login_page'))
    @method_decorator(staff_member_required(login_url=''))
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        vacancy.delete()
        return redirect('vacancy_list')


# @login_required(login_url='login_page')
# @staff_member_required
# def vacancy_list(request,pk):
#     form = VacancyFilterForm(request.GET)
#     vacancies = Vacancy.objects.all()
#
#     if form.is_valid():
#         employer = form.cleaned_data.get('employer')
#         if employer:
#             vacancies = vacancies.filter(employer=employer)
#
#     context = {
#         'form': form,
#         'vacancies': vacancies
#     }
#     return render(request, 'main_APP/vacansy_list_staff.html', context)