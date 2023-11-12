from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    rating = Column(Integer)
    comments = Column(String(255))

    order = relationship("Order", back_populates="feedback")

