from django.shortcuts import render
from bs4 import BeautifulSoup as bf 
from requests import get

# Create your views here.


def scarp():
    page = get('https://ndma.gov.in/en/alerts.html',verify=False)
    soup = bf(page.text,'html.parser')
    f = soup.find('ul',class_='latestnews')
    f=f.text
    o = f.find('FOR FURTHER')
    return f[:o]


def home(request):
    st = scarp()
    return render(request,'disaster/index.html',{'notification':st})
