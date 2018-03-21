from django.shortcuts import render, redirect


def index(request):
    return render(request=request, template_name='index.html')


def testUI(request):
    print('request :', request)
    print('request.GET :', request.GET)
    print('request.POST :', request.POST)
    return render(request=request, template_name='testUI.html')
