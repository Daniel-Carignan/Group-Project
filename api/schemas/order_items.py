from typing import Optional
from pydantic import BaseModel
from .orders import Order
from .dishes import Dishes


class OrderItemsBase(BaseModel):
    pass


class OrderItemsCreate(OrderItemsBase):
    order_id: int
    dish_id: int

class OrderItemsUpdate(BaseModel):
    order_id: Optional[int] = None
    dish_id: Optional[int] = None

class OrderItems(OrderItemsBase):
    id: int
    orders: list[Order] = None
    dishes: list[Dishes] = None

    class ConfigDict:
        from_attributes = True