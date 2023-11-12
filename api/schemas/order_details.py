from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order


class OrderDetailBase(BaseModel):
    first_name: str
    last_name: str
    customer_address: str


class OrderDetailCreate(OrderDetailBase):
    order_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    customer_address: Optional[str] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    first_name: str
    last_name: str
    customer_address: str
    orders: list[Order] = None

    class ConfigDict:
        from_attributes = True