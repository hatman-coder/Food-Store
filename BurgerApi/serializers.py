from rest_framework import serializers
from .models import *
from rest_framework import parsers


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


class AddOnesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOnes
        exclude = ['id']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AddOnesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOnes
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    addOnes = AddOnesSerializer()

    class Meta:
        model = Product
        exclude = ['in_stock']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        addOnes_data = validated_data.pop('addOnes')
        category = CategorySerializer.create(CategorySerializer(), validated_data=category_data)
        addOnes = AddOnesSerializer.create(AddOnesSerializer(), validated_data=addOnes_data)
        make, created = Product.objects.update_or_create(category=category, addOnes=addOnes,
                                                         img=validated_data.pop('img'), name=validated_data.pop('name'),
                                                         price=validated_data.pop('price'))
        return make


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    # products = ProductSerializer()
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'customer']

    def create(self, validated_data):
        customerData = validated_data.pop('customer')
        customer = CustomerSerializer.create(CustomerSerializer(), validated_data=customerData)
        order, created = Order.objects.update_or_create(
            customer=customer,
            products=validated_data.pop('products'),
            user=validated_data.pop('user')
        )
        return order
