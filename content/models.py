import uuid
from django.db import models
import random
from django.conf import settings
from django.db import models
from django.urls import reverse
# Create your models here.

random_string = str(random.randint(1000000000,9999999999))

class Waybill(models.Model):
    STATUS_CHOICES = (
        ('in transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('delivery problem', 'Delivered Problem'),
        ('refunded', 'Refunded'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='waybill_created')
    name_of_goods = models.CharField(max_length=250)
    tracking_number =  models.CharField(max_length=10, default=random_string, editable=False)
    dispath_time = models.DateField(auto_now=False, auto_now_add=False)
    delivery_date = models.DateField(auto_now_add=False, auto_now=False)
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='in transit')

    def __str__(self):
        return self.name_of_goods

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])