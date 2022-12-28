from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_2']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Passwords should be the same')
        return data

    def create(self, validated_data):
        new_user = User(
            username =validated_data['username'],
            email = validated_data['email'],
        )
        new_user.set_password(validated_data['password'])
        #method set password wiill hash the password#
        new_user.save()
        return new_user
