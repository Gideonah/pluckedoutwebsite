from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):


	return render(request, 'pluckedsite/index.html')
	
def antichrist_view(request):


	return render(request, 'pluckedsite/antichrist.html')


def tracts_view(request):


	return render(request, 'pluckedsite/tracts.html')