from rest_framework import serializers


class VoiceSerrializers(serializers.Serializer):
    voice = serializers.FileField()