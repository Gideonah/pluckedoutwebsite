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

def hellfire_view(request):

	return render(request, 'studies/hellfire.html')

def sod_view(request):

	return render(request, 'studies/stateofthedead.html')

def israel_view(request):

	return render(request, 'studies/israel.html')

def ldstudies_view(request):

	return render(request, 'studies/biblestudy.html')

def sbholy_view(request):

	return render(request, 'studies/sabbathholy.html')

def alone_view(request):

	return render(request, 'studies/alone.html')

def prophecy_daniel2_view(request):

	return render(request, 'studies/dreamofaking.html')