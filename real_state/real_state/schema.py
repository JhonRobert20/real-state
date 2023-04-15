from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


def confirm_coordinate(value: str) -> str:
    """
    Validation to prevent corrupted coordinates field.
    Called by the helper function below;
    """
    if value:
        error = False
        coordinate = value.split(",")
        if len(coordinate) != 2:
            error = True
        else:
            try:
                float(coordinate[0])
                float(coordinate[1])
            except ValueError:
                error = True
        if error:
            raise ValueError("Coordinates must be in the format of 'lat,lng'.")

    return value


class EstateBase(BaseModel):
    build_status: Optional[str] = None
    is_active: Optional[bool] = None
    start_month: Optional[int] = None
    construction_type: Optional[int] = None
    date_diff: Optional[int] = None
    description: Optional[str] = None
    date_in: Optional[datetime] = None
    property_type: Optional[int] = None
    end_week: Optional[int] = None
    typology_type: Optional[int] = None
    id: str = None
    coordinates: Optional[str] = None
    boundary_id: Optional[str] = None
    id_uda: Optional[str] = None
    title: Optional[str] = None
    listing_type: Optional[int] = None
    date: Optional[datetime] = None

    _check_coordinate = validator("coordinates", allow_reuse=True)(confirm_coordinate)


class OrderBy(BaseModel):
    field: str
    direction: str


class PaginatedEstates(BaseModel):
    objects: List[EstateBase]
    page: int
    pages: int
    has_next: bool = False
    has_prev: bool = False
    order_by: Optional[OrderBy] = None
    total_results: Optional[int] = 0
