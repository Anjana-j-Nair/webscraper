from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from webscraperapp.models import Links

# Create your views here.

def home(request):
    if request.method=="POST":
        l_new=request.POST.get('page','')
    # urls=requests.get("http://www.google.com")
        urls=requests.get(l_new)
        b=BeautifulSoup(urls.text,'html.parser')
        for i in b.find_all('a'):
            l_address=i.get('href')
            l_name=i.string
            Links.objects.create(address=l_address,strname=l_name)
        # address.append(i.get('href'))
        return HttpResponseRedirect('/')
    else:
        data_values=Links.objects.all()
    return render(request,'home.html',{'ads':data_values})
