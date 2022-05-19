from django.shortcuts import render, HttpResponse
from Home.models import Contact
from datetime import datetime

# Create your views here.
#Views have the responsibility to carry data and render webpages
#Each function is associated with rendering a web page
"""
    This is where we render the templates.
"""
def index(request):
    context = {
        "message": "I am Nikhil!"
    } #This is simply the variable that we want to render in the index.html file. We are initialising
    #the variable
    return render(request, 'index.html', context) #Passing down the value of the variable down to the index.html file and rendering it
    #The render method takes in the request and the html file that we want to render.

def about(request):
    # return HttpResponse("This is the about page")
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
    # return HttpResponse("This is the contact page")
        return render(request, "status.html", {"status": "success", "msg": "Form successfully submitted", "flag": 1})
    else:
        return render(request, "contact.html")
