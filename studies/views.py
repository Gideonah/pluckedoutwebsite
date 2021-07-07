from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
import pdb
import pandas as pd
import difflib
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

def melchizedek_view(request):

	return render(request, 'studies/Melchizedek.html')

def dream_view(request):

	return render(request, 'studies/dreams.html')

def heaven_view(request):

	return render(request, 'studies/heaven.html')

def egwhite_view(request):

	return render(request, 'studies/EGWhite.html')

def symbolsearch_view(request):
	symbol_df = pd.read_csv("/home/pluckedout/pluckedoutwebsite/studies/symbols_database.csv")
	symbol_df["symbol"] = symbol_df["symbol"].apply(lambda x: x.strip())
	list_var = False
	variable = ''
	definitions = ''


	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:

		# check whether it's valid:
		def get_verses(symbol_df, variable):
			suggestions = False
			definitions = None
			verses = None

			if variable.lower() in symbol_df["symbol"].str.lower().unique():
				tmp = symbol_df[symbol_df['symbol'].str.lower() == variable].copy()
				verses = tmp["v_1"].values[0]
				definitions = tmp["definition"].values[0]
			else:
				suggestions = True
				tmp = symbol_df[symbol_df['symbol'].str.lower() == variable].copy()
				if len(tmp) == 0:
					definitions = "Cannot find any similar words"
				else:
					definitions = tmp["definition"].values[0]
				list_of_suggestions = difflib.get_close_matches(variable, symbol_df["symbol"].str.lower().unique())

			if suggestions:
				return (list_of_suggestions,definitions,"suggestions")
			else:
				return (verses,definitions,"verses")

		variable = request.POST['name']

		variable = variable.lower()
		variable = get_verses(symbol_df, variable)
		definitions = variable[1]
		if variable[2]=="suggestions":
			variable = "No scripture" if len(variable[0])==0 else variable[0]
		else:
			variable = variable[0]

		if type(variable) == list:
			list_var = True
			variable = ",".join(variable)
		render(request, 'studies/symbolsearch.html',{'variable':variable, 'definitions':definitions, 'list_var': list_var})

	# if a GET (or any other method) we'll create a blank form


	return render(request, 'studies/symbolsearch.html',{'variable':variable, 'definitions':definitions, 'list_var': list_var})








