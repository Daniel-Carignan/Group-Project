from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class UsedPromotion(Base):
    __tablename__ = "used_promotions"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=False)
