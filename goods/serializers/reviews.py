from common.mixins.serializers import ExtendModelMixinSerializer
from goods.models import Review


class ReviewListSerializer(ExtendModelMixinSerializer):
    class Meta:
        model = Review
        fields = ('author', 'country', 'rating', 'text',)
