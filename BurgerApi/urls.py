from rest_framework.routers import DefaultRouter
from django.urls import  path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'order', OrderViewSet)
router.register(r'product', ProductViewset)
router.register(r'category', CategoryViewset)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)