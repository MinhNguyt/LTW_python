from django.contrib import admin
from qlkhohang.models import (MATHANG, KHOMATHANG)


class KhoMatHangAdmin(admin.ModelAdmin):
    list_display = ('MatHang', 'SoLuong', 'Kho')
    list_filter = ('MatHang', 'SoLuong')


# Register your models here.
admin.site.register(MATHANG)
admin.site.register(KHOMATHANG, KhoMatHangAdmin)
