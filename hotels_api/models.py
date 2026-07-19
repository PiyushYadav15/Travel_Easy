# hotels/models.py

from django.db import models
from destinations.models import Destination

class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
