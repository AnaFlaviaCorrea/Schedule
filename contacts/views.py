from django.shortcuts import render, HttpResponse
from . models import Contacts


def index(request):
    contacts = Contacts.objects.all()
    return render(request, 'pages/index.html', {'contacts': contacts})

def search(request):
    busca = request.GET.get('search')
   
    contacts = Contacts.objects.filter(name__icontains = busca)
    return render(request, 'pages/index.html', {'contacts': contacts})
    

# HttpResponse('Olá mundo')
