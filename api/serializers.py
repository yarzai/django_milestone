from rest_framework import serializers


class FirstSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
