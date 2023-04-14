from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/estates/", response_model=str)
def get_multiple_estate(offset: int = 0, limit: int = 10) -> Any:
    """
    Endpoint to get multiple posts based on offset and limit values.
    """
    return "Welcome to the real state fastapi app"
