from typing import Optional
from pydantic import BaseModel

class OrderDetailBase(BaseModel):
    order_id: int
    first_name: str
    last_name: str
    customer_address: str


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    customer_address: Optional[str] = None


class OrderDetail(OrderDetailBase):
    id: int

    class ConfigDict:
        from_attributes = True