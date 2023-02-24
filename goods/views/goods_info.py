from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Good
from goods.serializers.article_serializer import ArticleInputSerializer
from scraping.scraping_for_wildberries import get_info_goods


class InfoGoodsView(APIView):

    def post(self, request):
        serializer = ArticleInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = get_info_goods(request.POST.get('article'))
        if not data:
            return Response({"error": "Проверьте артикул"},
                            status=status.HTTP_204_NO_CONTENT)
        return Response({
            "results": data
        }, status=status.HTTP_200_OK)


class GoodsSaveView(APIView):
    def get(self, request, goods_id):
        if request.user.is_anonymous:
            return Response({
                "errors": "Необходимо авторизоваться"
            }, status=status.HTTP_401_UNAUTHORIZED)
        data = get_info_goods(goods_id)
        if not data:
            return Response({"error": "Проверьте артикул"},
                            status=status.HTTP_204_NO_CONTENT)
        user = request.user
        good, created = Good.objects.get_or_create(
            user=user,
            **data
        )
        return Response({
            "results": f"Товар '{good.name}(Артикул: {good.goods_id})' успешно сохранен"
        }, status=status.HTTP_200_OK)
