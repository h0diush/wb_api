from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

User = get_user_model()


class RegistrationUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        )

    def _check_for_uniqueness(self, value):
        if User.objects.filter(email=value).exists():
            raise ParseError(
                'Пользователь с такой электронной почтой уже существует'
            )
        if User.objects.filter(username=value).exists():
            raise ParseError(
                'Пользователь с таким никнеймом уже существует'
            )
        return value

    def validate_email(self, value):
        return self._check_for_uniqueness(value)

    def validate_username(self, value):
        return self._check_for_uniqueness(value)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
