from django.shortcuts import render
from .forms import CurrencyForm
from requests import get
from decimal import Decimal, ROUND_UP


def index(request):
    list_choices = [
        (1, 'Українська гривня')
    ]
    response = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json').json()
    for item in response:
        list_choices.append((item['rate'], item['txt']))

    if request.method == 'POST':
        form = CurrencyForm(request.POST, choices=list_choices)
        if form.is_valid():
            currency1 = Decimal(form.cleaned_data['currency1'])
            currency2 = Decimal(form.cleaned_data['currency2'])
            count = Decimal(form.cleaned_data['count'])
            is_round = form.cleaned_data['round_num']
            result = count * currency1 / currency2
            if is_round:
                result = result.quantize(Decimal('0.00'), rounding=ROUND_UP)

        return render(request, 'index.html', {'form': form, 'result': result})
    else:
        form = CurrencyForm(choices=list_choices)
        return render(request, 'index.html', {'form': form})
