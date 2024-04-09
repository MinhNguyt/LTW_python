from django.shortcuts import render,get_object_or_404, redirect
from .models import KHO, KHOMATHANG
from .form import KhoForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def suakho(request,khoid=None):
    if khoid is not None:
        Kho = get_object_or_404(KHO,id=khoid)
    else:
        Kho = None
    if request.method == 'POST':
        form = KhoForm(request.POST, instance=Kho)
        if form.is_valid():
            Kho = form.save(commit=False)
            if khoid is None:
                messages.success(request, "Thêm kho mới thành công")
            else:
                messages.success(request, "Các thông tin điều chỉnh của kho {} đã được lưu lại",format(Kho.ten))
            Kho.save()
            return redirect('DanhsachHangHoa',id = khoid)
    else:
        form = KhoForm(instance=Kho)
    return render(request, 'suakho.html', {
        'form': form,
        'instance': Kho})
def dskho(request):
    kho= KHO.objects.all()
    return render(request,'dskho.html',{'kho':kho})
