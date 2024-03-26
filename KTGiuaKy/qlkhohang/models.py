from django.db import models

# Create your models here.
class MATHANG(models.Model):
    class DVTChoice(models.TextChoices):
        KG = "KG", "kg"
        CAI = "CAI", "kg"
        CHAI = "CHAI", "kg"
        HOP = "HOP", "kg"
    Ten = models.CharField(
        max_length=255,
        help_text="Ten cua mat hang"
    )
    MoTa = models.TextField()
    DVT = models.CharField(choices=DVTChoice.choices, max_length=20)

    def __str__(self):
        return self.Ten

class KHO(models.Model):
    Ten = models.CharField(max_length=255, help_text="Ten cua Kho")
    DiaChi = models.CharField(max_length=255)
    MatHang = models.ManyToManyField(
        'MATHANG',
        through="KHOMATHANG")
class KHOMATHANG(models.Model):
    MatHang = models.ForeignKey(
        MATHANG,
        on_delete= models.CASCADE
    )
    Kho = models.ForeignKey(
        KHO,
        on_delete= models.CASCADE
    )
    SoLuong = models.IntegerField(help_text="So luong cua mat hang")



