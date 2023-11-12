from typing import Optional
from pydantic import BaseModel
from .orders import Order



class FeedbackBase(BaseModel):
    rating: int
    comments: str


class FeedbackCreate(FeedbackBase):
    order_id: int


class FeedbackUpdate(BaseModel):
    order_id: Optional[int] = None
    rating: Optional[int] = None
    comments: Optional[str] = None

class Feedback(FeedbackBase):
    id: int
    order_id: int
    rating: int
    comments: str
    orders: list[Order] = None


    class ConfigDict:
        from_attributes = True