from django.shortcuts import render
from django.http import HttpResponse
import requests

def persons(request):

    response = requests.get('https://api.victorsanmartin.com/feriados/en.json')

    data = response.json()
    
    date = data['data']
    
    users = {
        'data' : data
    }

    return render(request, "feriados.html", {'feriados': date})
    pass




