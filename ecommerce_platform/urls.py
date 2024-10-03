from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api import AllergenViewSet, ProductViewSet, OrderViewSet
from profiles.api import UserProfileViewSet, WholesaleProfileViewSet

router = DefaultRouter()
router.register(r'allergens', AllergenViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'wholesale-profiles', WholesaleProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]