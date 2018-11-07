from django import forms
from food.models import *

class EditIngredientPriceForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.none(), required=False)

    class Meta:
        model = IngredientPrice
        fields = ['ingredient', 'price', 'quantity']
        exclude = ('status', 'date')

    def __init__(self, *args, **kwargs):
        super(EditIngredientPriceForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = Ingredient.objects.all()