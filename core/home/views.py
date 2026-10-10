from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):

    peoples = [
        {'name': "abin" , 'age' : 26},
        {"name" : "krishna" , "age" : 5},
        {"name" : "ram  hari" , "age" : 10},
        {"name" : "gopal ghimire " , "age" : 33}
    ]
    vegetables = ['pumpkin' , 'tomato', 'potato' ,'cocumber']

    return render(request, "home/index.html" , context = {'peoples':peoples , 'vegetables':vegetables}) #key value is first people  context shows data to html 

def success_page(request: HttpRequest) -> HttpResponse:
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page</h1>")