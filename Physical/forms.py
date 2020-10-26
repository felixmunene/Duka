from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Physical.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'product_model', 'quantity', 'entryprice','product_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save product'))
class UpdateProducts(forms.Form):
    name = forms.ChoiceField(choices=[(choice, choice) for choice in Products.objects.all()])
    
    quantity  = forms.IntegerField()

from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class saleform(forms.Form):
    Item = forms.CharField(max_length=25)
    Imei = forms.IntegerField()
    Price = forms.FloatField()
    #PaymentMethod = forms.CharField(max_length=10)