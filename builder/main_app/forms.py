from django.forms import ModelForm
from .models import Quotation

class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ['price']