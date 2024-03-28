from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'hote.html', {'name': "siva"})

def add (request):
    val1 = int(request.post['num1'])
    val2 = int(request.post['num2'])
    res = val1 + val2

    return render (request,"result.html", {"result":res})
