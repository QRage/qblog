from django.shortcuts import render


def resume_home(request):
    return render(request, 'resume.html')
