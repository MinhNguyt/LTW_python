from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import ThietBi
from .form import FormThietBi

# Create your views here.
def edit_thietbi(request,id=None):
    if id is not None:
        thietbi = get_object_or_404(ThietBi, id=id)
    else:
        thietbi = None
    if request.method == 'POST':
        form = FormThietBi(request.POST, instance=thietbi)
        if form.is_valid():
            update_thietbi = form.save(commit=False)
            if id is None:
                messages.success(request, "Thêm thiết bị '{}' thành công".format(thietbi))
            else:
                messages.success(request, "Thông tin thiết bị {} đã được lưu",format(thietbi.Ten))
            update_thietbi.save()
            return redirect('danhsachthietbi')
    else:
        form = FormThietBi(instance=thietbi)
    return render(request, 'edit_thietbi.html', {
        'form': form,
        'instance': thietbi})

def thietbi(request):
    thietbi = ThietBi.objects.all()
    return render(request,"dsthietbi.html",{"thietbi":thietbi})
def chonthietbi(request,id=None):
    chonthietbi = request.session.get('chonthietbi', [])
    if id is not None:
        thietbi = ThietBi.objects.get(id=id)
        ten = thietbi.Ten
        idchon = thietbi.id
        chonthietbi.append([idchon,ten])
        request.session['chonthietbi'] = chonthietbi
    return render(request,"dsthietbichon.html",{"chonthietbi":chonthietbi})


