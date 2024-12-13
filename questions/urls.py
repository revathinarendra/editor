# from django.urls import path
# from . import views

# urlpatterns = [
#     path('mcqs/', views.mcq_list, name='mcq_list'),  # URL to access the list of MCQs
# ]
from django.urls import path
from .views import SubjectViewSet, McqViewSet

# Define explicit URLs for SubjectViewSet
subject_list = SubjectViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

subject_detail = SubjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Define explicit URLs for McqViewSet
mcq_list = McqViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

mcq_detail = McqViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('api/subjects/', subject_list, name='subject-list'),
    path('api/subjects/<int:pk>/', subject_detail, name='subject-detail'),
    path('api/mcqs/', mcq_list, name='mcq-list'),
    path('api/mcqs/<int:pk>/', mcq_detail, name='mcq-detail'),
]
