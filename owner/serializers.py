from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from owner.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, password: str) -> str:
        """
            Validate password method is used for hashing the raw password
            before saving into the db
        """
        return make_password(password)
