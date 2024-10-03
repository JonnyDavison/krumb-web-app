from rest_framework import viewsets
from .models import UserProfile, WholesaleProfile
from .serializers import UserProfileSerializer, WholesaleProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class WholesaleProfileViewSet(viewsets.ModelViewSet):
    queryset = WholesaleProfile.objects.all()
    serializer_class = WholesaleProfileSerializer