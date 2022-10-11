from rest_framework import serializers
from .models import *
from rest_framework import parsers
import datetime


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


# class AddOnesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddOnes
#         exclude = ['id']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class AddOnesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddOnes
#         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['in_stock']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        addOnes_data = validated_data.pop('addOnes')
        make, created = Product.objects.update_or_create(category=category_data, addOnes=addOnes_data,
                                                         img=validated_data.pop('img'), name=validated_data.pop('name'),
                                                         price=validated_data.pop('price'))
        return make


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'customer', 'orderTime']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = CustomerSerializer.create(CustomerSerializer(), validated_data=customer_data)
        order, created = Order.objects.update_or_create(
            products=validated_data.pop('products'),
            user=validated_data.pop('user'),
            customer=customer
        )
        return order

    # def update(self, instance, validated_data):
    # customer = validated_data.pop('customer')
    # products = validated_data.pop('products')
    # user = validated_data.pop('user')
    # instance.user = validated_data.get('user', instance.user)
    # instance.customer = validated_data.get('customer', instance.customer)
    # instance.products = validated_data.get('products', instance.products)
    # instance.save()
    # return instance

    # order_mapping = {order.id: order for order in instance}
    # data_mapping = {item['id']: item for item in validated_data}
    # ret = []
    # for order_id, data in data_mapping.items():
    #     order = order_mapping.get(order_id, None)
    #     if order is None:
    #         ret.append((self.child.create(data)))
    #     else:
    #         ret.append(self.child.update(order, data))
    # for order_id, order in order_mapping.items():
    #     if order_id not in data_mapping:
    #         order.delete()
    # return ret
