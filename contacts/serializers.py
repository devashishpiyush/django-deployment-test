from rest_framework import serializers

from contacts import models


class ContactSerializer(serializers.ModelSerializer):
    """Serializes a Contact object."""
    class Meta:
        model = models.Contact
        fields = '__all__'
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
