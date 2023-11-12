from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order
from .promotions import Promotions


class UsedPromotionsBase(BaseModel):
    pass


class UsedPromotionsCreate(UsedPromotionsBase):
    order_id: int
    promotion_id: int

class UsedPromotionsUpdate(BaseModel):
    order_id: Optional[int] = None
    promotion_id: Optional[int] = None

class UsedPromotions(UsedPromotionsBase):
    id: int
    order_id: int
    promotion_id: int
    orders: list[Order] = None
    promotions: list[Promotions] = None

    class ConfigDict:
        from_attributes = True