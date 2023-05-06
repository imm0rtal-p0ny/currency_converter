from django import forms
import requests


class CurrencyForm(forms.Form):
    currency1 = forms.ChoiceField()
    currency2 = forms.ChoiceField()
    count = forms.FloatField()

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        a = kwargs.pop('a', None)

        super(CurrencyForm, self).__init__(*args, **kwargs)
        if choices:
            self.fields['currency1'].choices = choices
            self.fields['currency2'].choices = choices
        if a:
            self.fields['result'] = forms.IntegerField()




