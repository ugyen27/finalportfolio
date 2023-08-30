
from unicodedata import name
from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
      if request.method == "POST":
            name = request.POST.get('name',"")
            email = request.POST.get('email',"")
            project = request.POST.get('project',"")
            message = request.POST.get('message',"")
            con = Contact(name=name, email=email,project=project,message=message)
            con.save()
      return render (request, 'users/index.html',)