from django.db import models


class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    objects = None
    customer_id = models.CharField(max_length=50)
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_id}"


class OrderDetail(models.Model):
    objects = None
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey( Product, on_delete=models.CASCADE, related_name='order_details')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.product_name} - Order {self.order.id}"
