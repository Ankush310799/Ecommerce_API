from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from product.models import Product , UserProduct
from product.serializers import ProductSerializer , GetProductsInformationAnyone
from product.permissions import ForProductHandlingPermission,ForProductList

product_categories =(("Groccery","Groccery"),
                  ("Electronics","Electronics"),
                  ("Textile","Textile"),
                  ("Health","Health"),
                  ("Home_appliences","Home_appliences"),
                  ("Footwears","Footwears"),
                  ("Toy","Toy"),
                  ("Furniture","Furniture"),
                  ("other","other"),
                )


# Create your views here.
class ProductViewSet(ModelViewSet):

    queryset = Product.objects.none()
    serializer_class = ProductSerializer
    permission_classes = [ForProductHandlingPermission,]

    def create(self, request, *args, **kwargs):
        if request.POST._mutable is False:
            request.POST._mutable is True
        if request.user['is_owner']:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductListAPIViewSet(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = GetProductsInformationAnyone
    permission_classes = (AllowAny,)

    def get_queryset(self,):
        queryset = Product.objects.filter(not_interested=False).values("category").distinct()
        return queryset


# class AuthUserProductListAPIViewSet(generics.ListAPIView):

#     queryset = UserProduct.objects.all()
#     serializer_class = GetProductsInformationForAuthUser
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self,):
#         queryset = UserProduct.objects.filter(product__not_interested=False).values("product__category").distinct()
#         return queryset
