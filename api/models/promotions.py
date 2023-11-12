from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    promo_code = Column(String(255))
    discount = Column(DECIMAL(4, 2))



