from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from laspoteiros.users.api.views import UserViewSet
from laspoteiros.products.api.products import ProductViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("products", ProductViewSet, basename="products")



app_name = "api"
urlpatterns = router.urls
