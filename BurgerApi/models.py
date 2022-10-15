from email.policy import default
from re import T
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


def upload_product_image(instance, filename):
    return "uploads/{category}/{name}/{filename}".format(category=instance.category, name=instance.name,
                                                         filename=filename)


# https://stackoverflow.com/questions/36177385/visualizing-uploaded-images-in-django-admin


class Product(models.Model):
    addOns_list = (
        ('salad', 'Salad'),
        ('cheese', 'Cheese'),
        ('meat', 'Meat'),
        ('spice', 'Spice'),
        ('mayonnaise', 'Mayonnaise'),
    )

    img = models.ImageField(upload_to=upload_product_image, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=600)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    addons = MultiSelectField(choices=addOns_list, max_length=500)
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class CustomerDetail(models.Model):
    deliveryAddress = models.TextField(max_length=200, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    paymentType = models.CharField(max_length=20, blank=True
                                   )

    def __str__(self):
        return self.deliveryAddress


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    orderTime = models.DateTimeField(auto_now_add=True)
    addOns = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.products)
