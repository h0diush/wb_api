from django.urls import path, include

from goods.urls import urlpatterns as goods_urls
from users.urls import urlpatterns as users_urls

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += goods_urls
urlpatterns += users_urls
