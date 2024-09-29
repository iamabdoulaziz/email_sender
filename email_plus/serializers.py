from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class CvsSerializer(serializers.Serializer):
    file = serializers.FileField()

class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    created_at = serializers.DateTimeField()
