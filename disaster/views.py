from django.shortcuts import render
from bs4 import BeautifulSoup as bf
from requests import get
from django.views.generic import TemplateView,DetailView,CreateView
from .models import DisasterDetails
# Create your views here.


# class SignUp(CreateView):
#     form_class =
#     success_url=reverse_lazy('login')
#     template_name='disaster/signup.html'

def scarp():
    page = get('https://ndma.gov.in/en/alerts.html',verify=False)
    soup = bf(page.text,'html.parser')
    f = soup.find('ul',class_='latestnews')
    f=f.text
    o = f.find('FOR FURTHER')
    return f[:o]


def notify(request):
    st = scarp()
    return render(request,'disaster/index.html',{'notification':st})

def home(request):
    list = DisasterDetails.objects.all()
    return render(request,'disaster/home.html',{'list':list})

class DisasterDetailsView(DetailView):
    context_object_name = 'detail_list'
    model = DisasterDetails
    template_name='disaster/disaster_detail.html'
