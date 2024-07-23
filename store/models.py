from django.db import models


UNITS_CHOICES = (('G', 'Million Gold'),
                 ('C', 'Code(s)'))


class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    to_order = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    units = models.CharField(max_length=2, choices=UNITS_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    visible = models.BooleanField(default=True)
    default_order = models.IntegerField(default=0)

    def get_units(self):
        if self.price == 0:
            return ''
        elif self.units == 'G':
            return 'Million Gold'
        elif self.units == 'C':
            return 'Code(s)'
        return ''

    def __str__(self):
        return f'{self.name} [{self.qty}] @ {self.price} {self.get_units()}'
