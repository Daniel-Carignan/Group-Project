from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from datetime import datetime
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(255))
    total = Column(DECIMAL(4, 2))
    date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    
    customer_name = Column(String(255))
    customer_address = Column(String(255))
    customer_email = Column(String(255))
    customer_phone = Column(String(255))
    customer_comments = Column(String(255))
    
    payment_information = Column(String(255))
    payment_status = Column(String(255))
    payment_type = Column(String(255))

    items = relationship("OrderItem", backref="Order")
    promotion = relationship("UsedPromotion", backref="Order", uselist=False)

