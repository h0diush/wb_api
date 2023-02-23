from django.urls import path

from goods.views import goods_info

urlpatterns = [
    path('goods/', goods_info.InfoGoodView.as_view(), name='good-info'),
]
