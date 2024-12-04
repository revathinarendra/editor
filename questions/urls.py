from django.urls import path
from . import views

urlpatterns = [
    path('mcqs/', views.mcq_list, name='mcq_list'),  # URL to access the list of MCQs
]
