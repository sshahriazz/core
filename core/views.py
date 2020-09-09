from django.shortcuts import render


def my_resume(request):
    return render(request, 'core/resume.html', {'page_title': 'Resume'})


def home(request):
    return render(request, 'core/home.html', {'page_title': "Home"})
