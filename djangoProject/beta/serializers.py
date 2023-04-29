from rest_framework import serializers


class InputSerrializers(serializers.Serializer):
    input = serializers.CharField(max_length=100)