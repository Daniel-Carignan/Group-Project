from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    details_id = Column(Integer, ForeignKey("order_details.id"), nullable=False)
    payment_status = Column(String(255)) #change to an enum later

    order = relationship("Order", back_populates="payments")
    order_details = relationship("OrderDetail", back_populates="payments")
