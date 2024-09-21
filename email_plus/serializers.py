from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class CvsSerializer(serializers.Serializer):
    file = serializers.FileField()
