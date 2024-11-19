from .models import KHO
from django import forms

class KhoForm(forms.ModelForm):
    class Meta:
        model = KHO
        fields = "__all__"
