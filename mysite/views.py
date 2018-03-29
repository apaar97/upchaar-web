from django.shortcuts import render, redirect


def index(request):
    return render(request=request, template_name='index.html')


