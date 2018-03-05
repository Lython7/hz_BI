from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    uname = serializers.CharField()
    upassword = serializers.CharField()