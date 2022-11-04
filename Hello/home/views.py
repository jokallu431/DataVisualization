from django.shortcuts import render, HttpResponse
import pandas as pd

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my homepage")

def about(request):
     return render(request, 'about.html')

def services(request):
     if request.method == 'POST' and request.FILES['myfile']:
          myfile = request.FILES['myfile']
          fs = FileSystemStorage()
          filename = fs.save(myfile.name, myfile)
          uploaded_file_url = fs .url(filename)
          return render(request, 'services.html',{'uploaded_file_url': uploaded_file_url})
     return render (request,'services.html')
def gallery(request):
      return render(request, 'gallery.html')

def contact(request):
     return render(request, 'contact.html')