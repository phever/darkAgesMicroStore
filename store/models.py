from django.db import models


UNITS_CHOICES = (("G", "Million Gold"), ("C", "Code(s)"), ("D", "USD"))


class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    to_order = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    units = models.CharField(max_length=2, choices=UNITS_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/")
    visible = models.BooleanField(default=True)
    default_order = models.IntegerField(default=0)

    def get_units(self):
        if self.price == 0:
            return ""
        elif self.units == "G":
            return "Million Gold"
        elif self.units == "C":
            return "Code(s)"
        elif self.units == "D":
            return "USD"
        return ""

    def __str__(self):
        qty = self.qty
        if self.to_order:
            qty = "∞"
        visible = ""
        if not self.visible:
            visible = "HIDDEN - "
        return f"{visible}{self.name} [{qty}] @ {self.price} {self.get_units()}"
