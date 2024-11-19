from django.db import models

# Create your models here.
class DonVi(models.Model):
    Ten = models.CharField(max_length=255, null=False)
    DiaChi = models.CharField(max_length=100)

    def __str__(self):
        return self.Ten
class LoaiThietBi(models.Model):
    Ten = models.CharField(max_length=255, null=False)
    CacDonViSuDung = models.ManyToManyField(
        "DonVi", through="ThietBi"
    )
    def __str__(self):
        return self.Ten
class ThietBi(models.Model):
    Ten = models.CharField(max_length=255, null=False)
    ThongSoKyThuat =  models.TextField()
    DonViSuDung = models.ForeignKey(
        DonVi,
        on_delete=models.CASCADE,
        null=False
    )
    LoaiThietBi = models.ForeignKey(
        LoaiThietBi,
        on_delete=models.CASCADE,
        null=False
    )
    NgayBanGiao = models.DateField(null=False)
    class TinhTrangChoices(models.TextChoices):
        DangSuDung = "DangSuDung","Dangsudung"
        HuHong = "HuHong","Huhong"
        ThanhLy = "ThanhLy","Thanhly"
    TinhTrang = models.CharField(max_length=50,choices=TinhTrangChoices.choices,null=False)

    def __str__(self):
        return self.Ten
