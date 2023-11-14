from sqlalchemy import Column, ForeignKey, Integer, String
from ..dependencies.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    rating = Column(Integer)
    comments = Column(String(255))
