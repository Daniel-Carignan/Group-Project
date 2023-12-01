from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_item import OrderItem
from .promotion import Promotion


class OrderBase(BaseModel):
    status: str
    total: Optional[float] = 0
    date: Optional[datetime] = datetime.now()
    
    customer_name: str
    customer_address: str
    customer_email: str
    customer_phone: str
    customer_comments: str
    
    payment_information: str
    payment_status: str
    payment_type: str

class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_comments: Optional[str] = None
    order_status: Optional[str] = None
    order_total: Optional[float] = None
    order_date: Optional[datetime] = None
    
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    
    payment_information: Optional[str] = None
    payment_status: Optional[str] = None
    payment_type: Optional[str] = None


class Order(OrderBase):
    id: int
    
    items: list[OrderItem]
    promotion: Optional[Promotion]

    class ConfigDict:
        from_attributes = True
