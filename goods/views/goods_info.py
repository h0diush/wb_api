from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.mixins.views import CRDViewMixin
from goods.models import Good
from goods.serializers.goods import GoodsListSerializer, GoodsCreateSerializer, \
    GoodsRetrieveSerializer


class GoodsListForUserView(CRDViewMixin):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return GoodsCreateSerializer
        if self.action == 'retrieve':
            return GoodsRetrieveSerializer
        return GoodsListSerializer

    def get_queryset(self):
        return Good.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer = self.get_serializer(data=request.data,
                                         context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "results": serializer.OUTPUT_DATA
        })
