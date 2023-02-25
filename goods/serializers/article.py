from rest_framework import serializers
from rest_framework.exceptions import ParseError


class ArticleInputSerializer(serializers.Serializer):
    article = serializers.CharField(required=True, max_length=16,
                                    label="Артикул товара")

    def validate_article(self, value):
        if not value.isdigit():
            raise ParseError({
                "error": "Артикул должен состоять из цифр",
            })
        return value
