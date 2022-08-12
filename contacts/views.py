from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from contacts import (
    serializers,
    models,
    permissions,
)


# Create your views here.
class ContactViewSet(ModelViewSet):
    """Handles creating, reading and updating contacts."""

    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnContact, IsAuthenticated,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)
