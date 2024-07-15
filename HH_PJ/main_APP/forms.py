from django import forms
from django.contrib.auth.models import User

from .models import Resume, Vacancy, Company

class ResumeCreateForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['dream_job', 'name', 'surname', 'lastname', 'date_of_birth', 'email', 'phone', 'skills', 'exp', 'education', 'gender']

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['dream_job', 'name', 'surname', 'lastname', 'date_of_birth', 'email', 'phone', 'skills', 'exp', 'education', 'gender']

class VacancyCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'salary', 'skills', 'description', 'type_of_job']

class VacancyUpdateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'salary', 'skills', 'description', 'type_of_job']

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address']

class VacancyFilterForm(forms.Form):
    employer = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), required=False, label='Работодатель')