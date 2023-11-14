from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .feedback import Feedback
from .order_detail import OrderDetail
from .order_item import OrderItem
from .payment import Payment
from .used_promotions import UsedPromotion


class OrderBase(BaseModel):
    customer_comments: Optional[str] = None
    order_status: Optional[str] = None
    order_total: Optional[float] = None
    

class OrderCreate(OrderBase):
    # TODO: is feedback, detail, items etc needed here or should they be
    # handled separately or through the ORM?
    pass


class OrderUpdate(BaseModel):
    order_date: Optional[datetime] = None
    pass


class Order(OrderBase):
    id: int
    order_date: datetime
    
    feedback: Optional[Feedback]
    order_detail: OrderDetail
    items: list[OrderItem]
    payment: Payment
    used_promotion: Optional[UsedPromotion]
    
    
    class ConfigDict:
        from_attributes = True
