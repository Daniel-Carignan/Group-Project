from typing import Optional
from pydantic import BaseModel
from .orders import Order
from .dishes import Dishes


class RecipeBase(BaseModel):
    pass


class RecipeCreate(RecipeBase):
    order_id: int
    dish_id: int

class RecipeUpdate(BaseModel):
    order_id: Optional[int] = None
    dish_id: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    orders: list[Order] = None
    dishes: list[Dishes] = None

    class ConfigDict:
        from_attributes = True