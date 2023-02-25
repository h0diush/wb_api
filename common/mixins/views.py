from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from goods.serializers.article import ArticleInputSerializer
from scraping.scraping_for_wildberries import GetReviewsProduct


class ExtendedGenericViewSet(GenericViewSet):
    pass


class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass


class ReadViewMixin(ExtendedGenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    ):
    pass


class CRDViewMixin(ReadViewMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    pass


class ReviewsGoodsMixin(APIView, GetReviewsProduct):
    def response_if_not_data(self):
        return Response({"error": "Проверьте артикул"},
                        status=status.HTTP_204_NO_CONTENT)

    def response_if_user_is_anonymous(self):
        return Response({
            "errors": "Необходимо авторизоваться"
        }, status=status.HTTP_401_UNAUTHORIZED)


class CheckReviewGoodsMixin(ReviewsGoodsMixin):
    model = None

    def post(self, request):
        serializer = ArticleInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = self.get_info_goods(request.POST.get('article'))
        if not product:
            return self.response_if_not_data()
        if self.model == 'goods':
            return Response({
                "results": product
            }, status=status.HTTP_200_OK)
        elif self.model == 'reviews':
            data = self.get_reviews_data(product['root_id'])
            return Response({
                "count": len(data),
                "results": data
            }, status=status.HTTP_200_OK)
