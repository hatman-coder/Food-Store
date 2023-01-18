from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from BurgerApi import views

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'product', ProductViewset)
router.register(r'category', CategoryViewset)
router.register(r'addOns', AddOnsViewSet)
router.register(r'orderDetail', OrderDetailViewset)
router.register(r'orderMaster', OrderMasterViewset)
router.register(r'orderStatus', OrderStatusViewset)
router.register(r'paymentType', PaymentTypeViewset)


urlpatterns = [
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('addOns/filter/', CategorizedAddOnsViewSet.as_view(), name='addOns')
              ] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
