from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def success_page(request: HttpRequest) -> HttpResponse:
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page</h1>")