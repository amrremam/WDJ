from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'dashboard/dashboard.html')

def signin(request):
    return render(request, 'dashboard/sign-in.html')

# def tables(request):
#     return render(request, 'dashboard/tables.html')