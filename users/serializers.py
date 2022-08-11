from rest_framework import serializers

from users import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a UserProfile object."""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Update an exesting user."""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
