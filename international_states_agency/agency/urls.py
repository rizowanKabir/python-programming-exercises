from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.case_studies_list, name='case_studies_list'),
    path('work/<slug:slug>/', views.case_study_detail, name='case_study_detail'),
    path('api/lead/submit/', views.submit_lead_contact, name='submit_lead_contact'),
]
