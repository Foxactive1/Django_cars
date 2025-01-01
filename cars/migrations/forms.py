from django import forms
from .models import Car, Brand

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            raise forms.ValidationError('O preço do carro não pode ser menor do que R$20.000,00.')
        return price

class CarSearchForm(forms.Form):
    search = forms.CharField(required=False)