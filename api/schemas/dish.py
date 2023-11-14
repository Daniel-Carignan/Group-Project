from typing import Optional
from pydantic import BaseModel
from .dish_ingredient import DishIngredient

class DishBase(BaseModel):
    dish_name: str
    dish_description: str
    dish_price: float
    
class DishCreate(DishBase):
    pass


class DishUpdate(BaseModel):
    dish_name: Optional[str] = None
    dish_description: Optional[str] = None
    dish_price: Optional[float] = None


class Dish(DishBase):
    id: int
    ingredients: list[DishIngredient]
    
    class ConfigDict:
        from_attributes = True
