from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def study_view(request):

	return render(request, 'studies/studies.html')