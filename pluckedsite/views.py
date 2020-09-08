from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):


	return render(request, 'pluckedsite/index.html')
	
def construction_view(request):


	return render(request, 'pluckedsite/construction.html')