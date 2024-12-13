# from django.shortcuts import render
# from .models import Mcq

# def mcq_list(request):
#     mcqs = Mcq.objects.all()  # Fetch all MCQs from the database
#     return render(request, 'mcq.html', {'mcqs': mcqs})
# views.py
from rest_framework import viewsets
from .models import Subject, Mcq
from .serializers import SubjectSerializer, McqSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class McqViewSet(viewsets.ModelViewSet):
    queryset = Mcq.objects.all()
    serializer_class = McqSerializer
