from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    promo_code = Column(String(255))
    discount = Column(DECIMAL(4, 2))
