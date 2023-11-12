from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class OrderBase(BaseModel):
    customer_comments: str
    order_status: str
    order_total: str

class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_comments: Optional[str] = None
    order_status: Optional[str] = None
    order_total: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
