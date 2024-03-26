from django import forms
from .models import Publisher,Book
from .models import Review

SEARCH_CHOICES=(
    ("Value One","Title"),
    ("Value Two", "Contributor")
)
class SearchForm(forms.Form):
    search= forms.CharField(min_length=3)
    search_in=forms.ChoiceField(choices=SEARCH_CHOICES)
class PublisherForm(forms.ModelForm):
 class Meta:
     model = Publisher
     fields = "__all__"
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        label='Rating',
        min_value=0,
        max_value=5,  # Sử dụng HiddenInput() cho trường rating
    )

    class Meta:
        model = Review
        exclude = ['date_edited', 'book']
class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['cover', 'sample']