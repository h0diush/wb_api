from django.urls import path, include
from rest_framework.routers import DefaultRouter

from goods.views import goods_check, goods_info, reviews_check

router = DefaultRouter()

router.register('list', goods_info.GoodsListForUserView, basename='goods-list')

urlpatterns = [
    path('goods/', include(router.urls)),
    path('goods/check/', goods_check.InfoGoodsView.as_view(),
         name='good-check'),
    path('reviews/check/',
         reviews_check.GoodsReviewView.as_view(),
         name='reviews-check')
]
