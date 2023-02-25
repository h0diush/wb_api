from common.mixins.views import CheckReviewGoodsMixin


class InfoGoodsView(CheckReviewGoodsMixin):
    model = 'goods'
