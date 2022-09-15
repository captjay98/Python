from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    context = { 'recipes': recipes}
    return render(request, "main_recipe/index.html", context)

def about(request):
    return render(request, "main_recipe/about.html")