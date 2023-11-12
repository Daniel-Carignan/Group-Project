from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class UsedPromotions(Base):
    __tablename__ = "used_promotions"

    id = Column(Integer, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=False)

    order = relationship("Order", back_populates="used_promotions")
    promotions = relationship("Promotions", back_populates="used_promotions")
