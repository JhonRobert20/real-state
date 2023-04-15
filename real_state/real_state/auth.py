from fastapi import HTTPException, Request
from users.models import User


def is_logged(request: Request):
    cookies = request.cookies
    user_id = cookies.get("user_id")
    if not user_id:
        return False

    exists_user = User.objects.filter(id=user_id).exists()
    if not exists_user:
        raise HTTPException(status_code=401, detail="Not logged")
