from django.db import transaction
from faker.providers.date_time import ParseError
from rest_framework import serializers

from common.mixins.serializers import ExtendModelMixinSerializer
from goods.models import Good, Review
from goods.serializers.article import ArticleInputSerializer
from goods.serializers.reviews import ReviewListSerializer
from scraping.scraping_for_wildberries import GetReviewsProduct


class GoodsListSerializer(ExtendModelMixinSerializer):
    class Meta:
        model = Good
        fields = (
            "name",
            "price",
            "goods_id",
            "root_id",
            "date"
        )


class GoodsCreateSerializer(ArticleInputSerializer, GetReviewsProduct):
    OUTPUT_DATA = []

    def create(self, validated_data):
        article = validated_data.pop('article')
        product_data = self.get_info_goods(article)
        if not product_data:
            return ParseError({"errors": "Продукт не найден"})
        reviews = self.get_reviews_data(product_data['root_id'])
        with transaction.atomic():
            good, created = Good.objects.get_or_create(
                user=self.context['request'].user, **product_data
            )
            if created:
                for review in reviews:
                    rev, _ = Review.objects.get_or_create(
                        good=good,
                        **review
                    )
                    if _:
                        rev.save()
                good.save()
            self.OUTPUT_DATA.append(product_data)
            return product_data


class GoodsRetrieveSerializer(ExtendModelMixinSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Good
        fields = ('name', 'price', 'goods_id', 'root_id', 'date', 'reviews')

    def get_reviews(self, obj):
        qs = Review.objects.filter(good=obj)
        return ReviewListSerializer(qs, many=True).data
