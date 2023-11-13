from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DishesBase(BaseModel):
    dish_name: str
    dish_description: str
    dish_price: float


class DishesCreate(DishesBase):
    pass


class DishesUpdate(BaseModel):
    dish_name: Optional[str] = None
    dish_description: Optional[str] = None
    dish_price: Optional[float] = None


class Dishes(DishesBase):
    id: int
    dish_name: str
    dish_description: str
    dish_price: float

    class ConfigDict:
        from_attributes = True
