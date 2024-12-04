from django.shortcuts import render
from .models import Mcq

def mcq_list(request):
    mcqs = Mcq.objects.all()  # Fetch all MCQs from the database
    return render(request, 'mcq.html', {'mcqs': mcqs})
