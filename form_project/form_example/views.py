from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

initial = {"email": "user@example.com"}
def form_example(request):
  if request.method == "POST":
   form = OrderForm(request.POST, initial=initial)
   if form.is_valid():
    for name, value in form.cleaned_data.items():
     print("{}: ({}) {}".format(name, type(value), value))
  else:
   form = OrderForm(initial=initial)
  return render(request, "form-example.html", {"method": request.method, "form": form})


