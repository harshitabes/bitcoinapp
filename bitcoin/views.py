from django.shortcuts import render
import requests
from .models import Person

def home(request):
    var=Person.objects.all()
    context={'data':var}
    return render(request,'bitcoin/bit.html',context)


def price(request):
    if request.method == 'POST':
        var = Person(username=request.POST['name'], currency=request.POST['Currency'])
        var.save()
        #return redirect('price')
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    y = r.json()['bpi']

    '''for key, value in y.items():
        print(key,value['rate'])'''

    detail=var.currency
    data = y[detail]['rate']
    context={'data': data,'detail':detail}

    return render(request, 'bitcoin/price.html', context)
