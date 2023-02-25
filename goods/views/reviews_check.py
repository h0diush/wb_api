from common.mixins.views import CheckReviewGoodsMixin


class GoodsReviewView(CheckReviewGoodsMixin):
    model = 'reviews'
