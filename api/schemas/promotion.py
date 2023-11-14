from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promo_code: str
    discount: float


class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    discount: Optional[float] = None


class Promotion(PromotionBase):
    id: int
    promo_code: str
    discount: float

    class ConfigDict:
        from_attributes = True