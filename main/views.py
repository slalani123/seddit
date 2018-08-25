from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.html')
def gaming(request):
    return render(request, 'main/gaming.html')
def humor(request):
    return render(request, 'main/humor.html')
def programing(request):
    return render(request,'main/programing.html')
def tech(request):
    return render(request, 'main/tech.html')
def login(request):
    return render(request, 'main/login.html')


