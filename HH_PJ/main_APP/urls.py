from django.urls import path
from .views import (
    StartPageView,
    VacancyListView,
    VacancyDetailView,
    VacancyCreateView,
    VacancyUpdateView,
    VacancyDeleteView,
    ResumeListView,
    ResumeDetailView,
    ResumeCreateView,
    ResumeUpdateView,
    ResumeDeleteView,
)

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancies/<int:pk>/delete/', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('resumes/', ResumeListView.as_view(), name='resume_list'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('resumes/create/', ResumeCreateView.as_view(), name='resume_create'),
    path('resumes/<int:pk>/update/', ResumeUpdateView.as_view(), name='resume_update'),
    path('resumes/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),
]
