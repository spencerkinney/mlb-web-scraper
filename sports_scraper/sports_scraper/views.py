from django.shortcuts import render, HttpResponse
import requests
from .functions import get_hitters_information, get_pitchers_information

def hitters(request):
    hitters_url = 'https://www.mlb.com/stats/hitting'
    hitters_list = get_hitters_information(hitters_url)
    return render(request, 'index.html', {'hitters_list': hitters_list})

def pitchers(request):
    pitchers_url = 'https://www.mlb.com/stats/pitching'
    pitchers_list = get_pitchers_information(pitchers_url)
    return render(request, 'index.html', {'pitchers_list': pitchers_list})

def index(request):
    return render (request, 'index.html')