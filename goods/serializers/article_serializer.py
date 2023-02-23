from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.mixins.serializers import ExtendModelMixinSerializer
from goods.models import Good


class ArticleInputSerializer(serializers.Serializer):
    article = serializers.CharField(required=True, max_length=16)

    def validate_article(self, value):
        if not value.isdigit():
            raise ParseError({
                "error": "Артикул должен состоять из цифр",
            })
        return value


class GoodCreateSerializer(ExtendModelMixinSerializer):
    class Meta:
        model = Good
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):
    author = serializers.CharField()
    country = serializers.CharField()
    text = serializers.CharField()
    rating = serializers.CharField()
