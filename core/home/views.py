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

    for people in peoples:
        if people['age']:
            print("Yes")
    vegetables = ['pumpkin' , 'tomato', 'potato' ,'cocumber']

    return render(request, "home/index.html" , context = {'page': "Home",'peoples': peoples , 'vegetables':vegetables}) #key value is first people  context shows data to html 

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")

def about(request):
    context = {"page" : "About"}

    return render(request, "home/about.html",context )

def contact(request):
    context = {"page" : "Contact"}
    return render(request, "home/contact.html",context)
