from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm

def index_view(request):
    return render(request, 'testapp/home.html')

def add_movie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'testapp/addmovie.html', {'form':form})

def list_movie(request):
    movie_list=Movie.objects.all()
    return render(request, 'testapp/movielist.html', {'movie_list': movie_list})
