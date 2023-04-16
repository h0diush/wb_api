from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models.profiles import CodeForTelegram
from users.serializers import users as users_s

User = get_user_model()


class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = users_s.RegistrationUserSerializer


class GenerateCodeForTelegram(APIView):

    def get(self, request, *ergs, **kwargs):
        message = """Внимание код девяти значное число. Данный код необходимо ввести в телеграмме -> /reg ваш_код."""
        if request.user.is_anonymous:
            return Response({"errors": "Необходимо авторизоваться"},
                            status=status.HTTP_403_FORBIDDEN)
        if request.user.telegram_id:
            return Response({'results': 'Вы уже авторизованны'},
                            status=status.HTTP_204_NO_CONTENT)
        code_for_telegram, create = CodeForTelegram.objects.get_or_create(
            user=request.user
        )
        if create:
            code_for_telegram.save()
        return Response({'results': f'{code_for_telegram.hash_code}',
                         'message': message},
                        status=status.HTTP_200_OK)
