from rest_framework import serializers


class ExtendModelMixinSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
