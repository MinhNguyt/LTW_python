from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm
from .models import ExampleModel
from PIL import Image
# Create your views here.
def media_example(request):
  instance = None
  if request.method == "POST":
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save()
    #   instance = ExampleModel()
    #   instance.image_field = form.cleaned_data["image_upload"]
    #   instance.file_field = form.cleaned_data["file_upload"]
    #   instance.save()
      # save_path = settings.MEDIA_ROOT /request.FILES["file_upload"].name
      #
      # # image = Image.open(form.cleaned_data["file_upload"])
      # # image.thumbnail((50, 50))
      # # image.save(save_path)
      # with open(save_path, "wb") as output_file:
      #   for chunk in form.cleaned_data["file_upload"].chunks():
      #     output_file.write(chunk)
  else:
    form = UploadForm()
  return render(request,'media-example.html',{"form":form,"instance": instance})