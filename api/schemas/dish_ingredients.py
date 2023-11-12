from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .dishes import Dishes

class DishIngredientsBase(BaseModel):
    ingredient_name: str
    ingredient_description: str
    serving_size: int


class DishIngredientsCreate(DishIngredientsBase):
    dish_id: int


class DishIngredientsUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    ingredient_description: Optional[str] = None
    serving_size: Optional[int] = None
    dish_id: Optional[int] = None


class DishIngredients(DishIngredientsBase):
    id: int
    ingredient_name: str
    ingredient_description: str
    serving_size: str
    dish_id: int
    dishes: list[Dishes] = None
    class ConfigDict:
        from_attributes = True