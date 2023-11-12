from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionsBase(BaseModel):
    promo_code: str
    discount: float


class PromotionsCreate(PromotionsBase):
    pass

class PromotionsUpdate(BaseModel):
    promo_code: Optional[str] = None
    discount: Optional[float] = None


class Promotions(PromotionsBase):
    id: int
    promo_code: str
    discount: float

    class ConfigDict:
        from_attributes = True