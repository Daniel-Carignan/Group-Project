from typing import Optional
from pydantic import BaseModel

class DishIngredientBase(BaseModel):
    ingredient_name: str
    ingredient_description: str
    serving_size: int
    dish_id: int


class DishIngredientCreate(DishIngredientBase):
    pass


class DishIngredientUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    ingredient_description: Optional[str] = None
    serving_size: Optional[int] = None
    dish_id: Optional[int] = None


class DishIngredient(DishIngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True