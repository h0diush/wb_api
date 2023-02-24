from django.urls import path

from goods.views import goods_info

urlpatterns = [
    path('goods/', goods_info.InfoGoodsView.as_view(), name='good-info'),
    path('goods/<int:goods_id>/saved/', goods_info.GoodsSaveView.as_view(),
         name='good-save'),
]
