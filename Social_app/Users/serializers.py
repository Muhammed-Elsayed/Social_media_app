from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    date_of_birth = serializers.DateField(required=True)
    gender = serializers.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'gender']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
