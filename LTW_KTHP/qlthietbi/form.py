from django import forms
from .models import ThietBi

class FormThietBi(forms.ModelForm):
    class Meta:
        model = ThietBi
        fields = "__all__"