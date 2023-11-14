from typing import Optional
from pydantic import BaseModel
from .dish import Dish

class OrderItemBase(BaseModel):
    order_id: int
    dish_id: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    order_id: Optional[int] = None
    dish_id: Optional[int] = None

class OrderItem(OrderItemBase):
    id: int
    dish: Dish

    class ConfigDict:
        from_attributes = True