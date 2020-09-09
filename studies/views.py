from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def prayer_view(request):

	return render(request, 'studies/prayer.html')

def meeting_view(request):

	return render(request, 'studies/meeting.html')

def statement_view(request):

	return render(request, 'studies/statement.html')

def resources_view(request):

	return render(request, 'studies/resources.html')

def trinity_view(request):

	return render(request, 'studies/trinity.html')