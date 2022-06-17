from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def profile(request):
    return render(request, 'main/profile.html')


def view_post(request):
    return render(request, 'main/view_post.html')
