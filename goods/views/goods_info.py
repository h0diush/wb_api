from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.serializers.article_serializer import ArticleInputSerializer
from scraping.scraping_for_wildberries import get_info_goods


class InfoGoodView(APIView):

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
