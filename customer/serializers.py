from rest_framework import serializers
from customer.models import CustomerCart ,CustomerProductView



class CustomerProductsViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProductView
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerCart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    products_count = serializers.SerializerMethodField("get_cart_products_count")
    cart_products = serializers.SerializerMethodField("get_cart_products")


    def get_cart_products(self,obj):
        return CustomerCart.objects.filter(
                    action="Add To Cart").values().distinct()

    def get_cart_products_count(self,obj):
        return CustomerCart.objects.filter(
                    action="Add To Cart").values().distinct().count()

    class Meta:
        model = CustomerCart
        fields = ('products_count','cart_products')


class BuySerializer(serializers.ModelSerializer):

    products_count = serializers.SerializerMethodField("get_buy_products_count")
    buy_products = serializers.SerializerMethodField("get_buy_products")


    def get_buy_products(self,obj):
        return CustomerCart.objects.filter(action="Buy").values().distinct()

    def get_buy_products_count(self,obj):
        return CustomerCart.objects.filter(action="Buy").values().distinct().count()

    class Meta:
        model = CustomerCart
        fields = ('products_count','buy_products')
