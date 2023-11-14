from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    details_id: int
    payment_status: str


class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    details_id: Optional[int] = None
    payment_status: Optional[str] = None

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True