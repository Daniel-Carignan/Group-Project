from sqlalchemy import Column, ForeignKey, Integer, String
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    details_id = Column(Integer, ForeignKey("order_details.id"), nullable=False)
    payment_status = Column(String(255)) #change to an enum later
