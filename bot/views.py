from asgiref.sync import sync_to_async

from users.models.profiles import CodeForTelegram
from users.models.users import User
from .validations import validation_code


@sync_to_async()
def create_telegram_user(code: str, chat_id: str) -> bool:
    if not validation_code(code):
        return False
    try:
        user_id = CodeForTelegram.objects.get(
            hash_code=code
        )
        user = User.objects.get(id=user_id.user.id)
        user.telegram_id = chat_id
        user.save()
        user_id.delete()
        return True
    except CodeForTelegram.DoesNotExist:
        return False
