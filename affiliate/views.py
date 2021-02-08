from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def products2(request):
    return render(request, 'products2.html', {})


def products3(request):
    return render(request, 'products3.html', {})


def about(request):
    return render(request, 'about.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})
