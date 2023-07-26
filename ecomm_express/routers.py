from rest_framework import routers

from owner import views as owner_views
from product import views as product_views
from customer import views as customer_views




router = routers.DefaultRouter()
# owner app
router.register(r'register', owner_views.UserRegistrationAPI,
                basename='user_register')

#product app.
router.register(r'addproduct', product_views.ProductViewSet,
                basename='add_product')

# Customer app.
router.register(r'customer', customer_views.CustomerActionViewSet,
                basename='customer_action')
router.register(r'action_on_product', customer_views.CustomerActionOnProductsViewSet,
                basename='action_on_products')
