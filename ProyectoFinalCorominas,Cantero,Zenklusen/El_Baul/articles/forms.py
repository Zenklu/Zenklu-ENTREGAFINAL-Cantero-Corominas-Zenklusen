from django import forms

class Formulario_articulo(forms.Form):

    name = forms.CharField(max_length=40)
    price= forms.FloatField()
    description=forms.CharField(max_length=80)
    image = forms.ImageField(required = False)
    