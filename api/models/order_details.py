from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    customer_address = Column(String(255))

    order = relationship("Order", back_populates="order_details")
