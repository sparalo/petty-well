from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
from .models import Movie

def index(request):
    
    moviedb_api_key = "5aad99b2a39f2a006f6499fbf03b170f"
    movie_response = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={moviedb_api_key}")
    movie_json = json.loads(movie_response.text)
    for key, value in movie_json.items():
        print(key, ":", value)
    return render(request, 'movie/index.html', {'response':movie_json})
