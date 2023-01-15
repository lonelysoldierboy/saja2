from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'index.html')

def helper(request):
    return render(request, 'helper.html')

def victim(request):
    return render(request, 'victim.html')

def aqhbar(request):
    return render(request, 'aqhbar.html')