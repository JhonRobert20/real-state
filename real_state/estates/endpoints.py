from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from real_state.auth import is_logged

router = APIRouter()


@router.get("/estates/", response_model=str)
def get_multiple_estate() -> Any:
    """
    Endpoint to get multiple real states based on offset and limit values.
    """
    return "Welcome to the real state fastapi app"


@router.get("/items/")
async def read_confidential_info(logged: bool = Depends(is_logged)):
    if not logged:
        return HTTPException(status_code=401, detail="Not logged")
    return "Welcome to the real state fastapi app"
