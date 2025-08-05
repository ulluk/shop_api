from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

STARS = (
    (i, '* ' * i) for i in range(1, 6)    
)



class Review(models.Model):
    text = models.TextField(max_length=256)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)
    def __str__(self):
        return self.text
# Create your models here.
