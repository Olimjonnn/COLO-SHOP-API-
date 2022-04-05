from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'worker'),
        (2, 'user'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "User"
        verbose_name_plural = "Users"

class Logo(models.Model):
    image = models.ImageField(upload_to="Logo/")

class Slider(models.Model):
    image = models.ImageField(upload_to="Slider/")
    title = models.CharField(max_length=40)
    title = models.CharField(max_length=80)

class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Product/")
    price = models.IntegerField()
    sale_price = models.IntegerField(blank=True, null=True)
    sale = models.CharField(max_length=30, blank=True, null=True)
    is_new = models.BooleanField(default=False, blank=True, null=True)
    best_sellers = models.BooleanField(default=False)

    # Deal Of The Week
class Client(models.Model):
    name = models.CharField(max_length=100)
    debt = models.IntegerField(default=0)




class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Wishlist(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class BestSellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class MiniInfo(models.Model):
    image = models.ImageField(upload_to="MiniInfo/")
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=40)

class Blog(models.Model):
    image = models.ImageField(upload_to="Blog/")
    text = models.CharField(max_length=100)
    date = models.DateField()

class Newsletter(models.Model):
    email = models.EmailField()


class AboutUs(models.Model):
    text = models.TextField()
    facebook = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    telegram = models.CharField(max_length=500)
    skype = models.CharField(max_length=500)


