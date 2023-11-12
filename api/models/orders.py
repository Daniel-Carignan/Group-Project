from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_comments = Column(String(255))
    order_status = Column(String(255)) # change to an enum value later
    order_total = Column(DECIMAL(4, 2))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))


