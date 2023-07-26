from rest_framework import serializers
from product.models import Product,UserProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('category',)


class GetProductsInformationAnyone(serializers.ModelSerializer):

    products_count = serializers.SerializerMethodField("get_product_count")
    category_name = serializers.SerializerMethodField("get_category_name")
    product = serializers.SerializerMethodField("get_product_list")

    def get_product_count(self,obj):
        return Product.objects.filter(category=obj['category']).count()

    def get_category_name(self,obj):
        return Product.objects.filter(
                category=obj['category']).values_list("category",flat=True).distinct()

    def get_product_list(self,obj):
        if obj is not None:
            products = Product.objects.filter(category=obj['category'])
            return GetProductSerializer(products,many=True).data


    class Meta:
        model = Product
        fields = ('products_count','category_name','product',)


# for authenticated user - after signup

# class GetUserProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProduct
#         fields = '__all__'

# class GetProductsInformationForAuthUser(serializers.ModelSerializer):

#     products_count = serializers.SerializerMethodField("get_product_count")
#     category_name = serializers.SerializerMethodField("get_category_name")
#     product = serializers.SerializerMethodField("get_product_list")

#     def get_product_count(self,obj):
#         return UserProduct.objects.filter(product__category=obj['category']).count()

#     def get_category_name(self,obj):
#         return UserProduct.objects.filter(product__category=obj['category']).values_list("category",flat=True).distinct()

#     def get_product_list(self,obj):
#         if obj is not None:
#             products = UserProduct.objects.filter(product__category=obj['category'])
#             return GetUserProductSerializer(products,many=True).data


#     class Meta:
#         model = UserProduct
#         fields = ('products_count','category_name','product',)
