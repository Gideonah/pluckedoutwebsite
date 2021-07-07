"""pluckedout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pluckedsite import views as pluckedsite_views
from studies import views as study_view


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pluckedsite_views.index, name='index'),
    path('prayer/', study_view.prayer_view, name='prayer'),
    path('meeting/', study_view.meeting_view, name='meeting'),
    path('hellfire/', study_view.hellfire_view, name='hellfire'),
    path('stateofthedead/', study_view.sod_view, name='stateofthedead'),
    path('israel/', study_view.israel_view, name='israel'),
    path('statement/', study_view.statement_view, name='statement'),
    path('resources/', study_view.resources_view, name='resources'),
    path('biblestudy/', study_view.ldstudies_view, name='ldstudies'),
    path('trinity/', study_view.trinity_view, name='trinity'),
    path('keepingsabbath/', study_view.sbholy_view, name='keepingsabbath'),
    path('alone/', study_view.alone_view, name='alone'),
    path('dreamofaking/', study_view.prophecy_daniel2_view, name='dreamofaking'),
    path('Melchizedek/', study_view.melchizedek_view, name='Melchizedek'),
    path('dreams/', study_view.dream_view, name='dreams'),
    path('heaven/', study_view.heaven_view, name='heaven'),
    path('EllenWhite/', study_view.egwhite_view, name='egwhite'),
    path('tracts/', pluckedsite_views.tracts_view, name='tracts'),
    path('antichrist/', pluckedsite_views.antichrist_view, name='antichrist'),
    path('symbolsofrevelation/', study_view.symbolsearch_view, name='symbolsofrevelation'),
]
