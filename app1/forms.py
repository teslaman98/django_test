from django import forms
from app1.dash_apps.blockchain import now_display
from app1.models import Buy

# from app1.models import Assets


class HomeForm(forms.ModelForm):
    Buy_cash = forms.DecimalField()
    price = now_display()


    class Meta:
        model = Buy
        fields = ('Buy_cash',)


class HomeForm_two(forms.ModelForm):
    buy_btc = forms.DecimalField()
    price = now_display()

    class Meta:
        model = Buy
        fields = ('buy_btc',)
"""
class TableForm(forms.ModelForm):
    btc = forms.DecimalField()
    cash = forms.DecimalField()

    class Meta:
        model = Assets
        fields = ('btc', 'cash',)
"""
