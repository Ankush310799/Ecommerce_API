from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from customer.models import CustomerCart,CustomerProductView
from customer.serializers import CustomerSerializer,CartSerializer,BuySerializer,\
                            CustomerProductsViewSerializer
from product.models import Product ,UserProduct,NotInterested
from product.serializers import ProductSerializer

# Create your views here.

class CustomerActionOnProductsViewSet(ModelViewSet):

    queryset = CustomerProductView.objects.all()
    serializer_class = CustomerProductsViewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                if serializer.data["not_interested"] is False or serializer.data["not_interested"] is True:
                    product = Product.objects.get(pk=serializer.data["product"])
                    NotInterested.objects.create(content_object=product,created_by=request.user)

                return Response(data=serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                print(e)
                return Response(status=status.HTTP_401_UNAUTHORIZED)


class CustomerActionViewSet(ModelViewSet):

    queryset = CustomerCart.objects.none()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CartProductsListAPIViewSet(generics.ListAPIView):

    serializer_class = CartSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = CustomerCart.objects.filter(
                        action="Add To Cart").values("action").distinct()
        return queryset


class BuyProductsListAPIViewSet(generics.ListAPIView):

    serializer_class = BuySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = CustomerCart.objects.filter(
                        action="Buy").values("action").distinct()
        return queryset
