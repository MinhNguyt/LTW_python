from django.db import models

# Create your models here.
class MATHANG(models.Model):
    class DVTChoice(models.TextChoices):
        KG = "KG", "kg"
        CAI = "CAI", "cai"
        CHAI = "CHAI", "chai"
        HOP = "HOP", "hop"
    Ten = models.CharField(
        max_length=255,
        help_text="Ten cua mat hang",
        null= False
    )
    MoTa = models.TextField(null=True)
    DVT = models.CharField(choices=DVTChoice.choices, max_length=20)

    def __str__(self):
        return self.Ten

class KHO(models.Model):
    Ten = models.CharField(max_length=255, help_text="Ten cua Kho",null=False)
    DiaChi = models.CharField(max_length=255, null=True)
    MatHang = models.ManyToManyField(
        'MATHANG',
        through="KHOMATHANG")
    def __str__(self):
        return self.Ten
class KHOMATHANG(models.Model):
    MatHang = models.ForeignKey(
        MATHANG,
        on_delete= models.CASCADE, null=False
    )
    Kho = models.ForeignKey(
        KHO,
        on_delete= models.CASCADE, null=False
    )
    SoLuong = models.IntegerField(help_text="So luong cua mat hang",null=False)
    def __str__(self):
        return "{} ({}) ({})".format(self.MatHang, self.SoLuong,self.Kho)


