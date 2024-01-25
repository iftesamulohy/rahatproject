# myapp/forms.py
from django import forms

from products.models import Color, Size

class AddToCartForm(forms.Form):
    color = forms.ModelChoiceField(queryset=Color.objects.all(), required=False)
    size = forms.ModelChoiceField(queryset=Size.objects.all(), required=False)
    quantity = forms.IntegerField(min_value=1)
