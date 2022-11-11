from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Cart"
        ordering = ["date_added"]

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.CharField(max_length=250, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "CartItem"

    def sub_total(self):
        return 1290000 * self.quantity

    def __str__(self):
        return self.product
