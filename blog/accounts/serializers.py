from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name  = serializers.CharField()
    username   = serializers.CharField()
    email      = serializers.EmailField()
    password   = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username= data['username']).exists():
            raise serializers.ValidationError('username already exists')
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            username = validated_data.get('username').lower(),
            email = validated_data.get('email')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username   = serializers.CharField()
    password   = serializers.CharField()

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username does not exist')
        return data

    def get_token(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        print("user:", user)
        if not user:
            return {'message': 'invalid credentials', 'data': {}}
        
        refresh = RefreshToken.for_user(user)
        # return {'message': 'login success', 'data': {
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        # }}
        return {'message': 'login success', 'data': {
            'token': str(refresh.access_token),
        }}