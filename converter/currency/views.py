from django.shortcuts import render
from .forms import CurrencyForm
from requests import get


def index(request):
    list_choices = [
        (1, 'usdt'),
        (2, 'btc'),
        (3, 'uah'),
    ]
    response = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json').json()
    for item in response:
        list_choices.append((item['r030'], item['cc']))

    if request.method == 'POST':
        form = CurrencyForm(request.POST, choices=list_choices, a=1)
        currency1 = request.POST['currency1']
        currency2 = request.POST['currency2']
    else:
        form = CurrencyForm(choices=list_choices)

    return render(request, 'index.html', {'form': form})
