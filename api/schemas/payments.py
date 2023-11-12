from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order
from .order_details import OrderDetail


class PaymentsBase(BaseModel):
    payment_status: str


class PaymentsCreate(PaymentsBase):
    order_id: int
    details_id: int

class PaymentsUpdate(BaseModel):
    order_id: Optional[int] = None
    details_id: Optional[int] = None
    payment_status: Optional[str] = None

class Payments(PaymentsBase):
    id: int
    order_id: int
    details_id: int
    payment_status: str
    orders: list[Order] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True