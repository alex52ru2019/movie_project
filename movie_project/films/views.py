from django.shortcuts import render, redirect
from .models import films_posts
from .forms import films_postsForm

# Create your views here.
def index(request):
    films = films_posts.objects.all()
    return render(request, 'films/index.html', {'films': films})
def new_record(request):
    error = ""
    if request.method == "POST":
        form = films_postsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Неправильные данные"
    form = films_postsForm()
    return render(request, 'films/new_record.html', {'form': form, 'error': error})