from django.shortcuts import render
import requests
from .models import Person

def home(request):
    var=Person.objects.all()
    context={'data':var}
    return render(request,'bitcoin/bit.html', context)


def price(request):
    if request.method == 'POST':
        var = Person(username=request.POST['name'], currency=request.POST['Currency'])
        var.save()

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')





    url = 'https://v3.exchangerate-api.com/bulk/f5e10faef5cbc261feeab7fb/'
    con='USD'
    url += con



    response = requests.get(url)
    val = response.json()




    y = r.json()['bpi']



    detail=var.currency



    if detail == 'INR':
        data = y['USD']['rate']
        for i in range(0, len(data)):
            if data[i] == ',':
                pos = i
                break;

        s1 = ""
        s1 += data[0:pos]
        s1 += data[pos + 1:len(data)]
        s4 = float(s1)
        data = str(s4*val['rates']['INR'])

        context={'data': data, 'detail':detail}
        return render(request, 'bitcoin/price.html', context)

    else:
        data = y[detail]['rate']
        context = {'data': data, 'detail': detail,}
        return render(request, 'bitcoin/price.html', context)
