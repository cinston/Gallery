from django.shortcuts import render
from .models import Image, Location, Category

def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html', {'images': images, 'locations': locations})

def location(request,location):
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'location.html', {"location":selected_location,"images":images})


# def category(request):
#     category = Category.objects.all()
#     return render(request, 'location.html', {"category":category})


def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
    return render(request,'search.html',{"images":searched_images,"category":search_term})