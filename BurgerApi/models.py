import string

from django.db import models
from django.db.models import ForeignKey
from multiselectfield import MultiSelectField
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
import random


def random_string(size=10, chars=string.ascii_lowercase + string.digits):
    data = ''.join(random.choice(chars) for _ in range(size))
    return data


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
    add_ons_list = (
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
    add_ons = MultiSelectField(choices=add_ons_list, max_length=500)
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class CustomerDetail(models.Model):
    delivery_address = models.TextField(max_length=200, blank=True)
    contact_number = models.CharField(max_length=13, blank=True)
    payment_type = models.CharField(max_length=20, blank=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.delivery_address


class OrderMaster(models.Model):
    order_no = models.CharField(max_length=10,
                                blank=True,
                                editable=False,
                                unique=True,
                                default=random_string)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    customer_detail = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)


class OrderDetail(models.Model):
    order_master_id = models.ForeignKey(OrderMaster, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.CharField(max_length=10000)
    add_ons = models.CharField(max_length=100, blank=True)
    quantity = models.TextField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True, auto_created=True, editable=False)

    def __str__(self):
        return str(self.order_master_id.order_no)