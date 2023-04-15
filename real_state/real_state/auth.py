from fastapi import Request
from users.models import User


def is_logged(request: Request):
    cookies = request.cookies
    user_id = cookies.get("user_id")
    if not user_id:
        return False

    exists_user = User.objects.filter(id=user_id).exists()
    return exists_user
