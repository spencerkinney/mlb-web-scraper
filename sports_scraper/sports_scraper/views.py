from django.shortcuts import render, HttpResponse
import requests
from .functions import get_hitters_information, get_pitchers_information
import pickle

def hitters(request):
    hitters_list = []
    with open('hitters.data', 'rb') as file:
        hitters_list = pickle.load(file)
    return render(request, 'index.html', {'hitters_list': hitters_list})

def pitchers(request):
    pitchers_list = []
    with open('pitchers.data', 'rb') as file:
        pitchers_list = pickle.load(file)
    return render(request, 'index.html', {'pitchers_list': pitchers_list})

def refresh(request):
    hitters_url = 'https://www.mlb.com/stats/hitting'
    hitters_list = get_hitters_information(hitters_url)
    with open('hitters.data', 'wb') as file:
        pickle.dump(hitters_list, file)

    pitchers_url = 'https://www.mlb.com/stats/pitching'
    pitchers_list = get_pitchers_information(pitchers_url)
    with open('pitchers.data', 'wb') as file:
        pickle.dump(pitchers_list, file)
    return render(request, 'index.html')

def headtohead(request):
    return render(request, 'head-to-head.html')

def index(request):
    return render(request, 'index.html')