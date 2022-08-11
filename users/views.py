from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication

from users import (
    models,
    serializers,
    permissions,
)

# Create your views here.
class UserViewSet(ModelViewSet):
    """Handle UserProfile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth token."""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES