from django.db import models
from django.conf import settings


class Trades(models.Model):
    ItemSell = models.CharField(null=False, max_length=30, default='')
    ItemBuy = models.CharField(null=False, max_length=30, default='')
    Title =  models.CharField(null=False, max_length=15, default='No Title')
    ForSale = models.BooleanField()
    ContactInfo = models.CharField(null=False, max_length=25, default='')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )