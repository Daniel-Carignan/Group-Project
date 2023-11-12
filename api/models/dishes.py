from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    dish_name = Column(String(255))
    dish_description = Column(String(255))
    dish_price = Column(DECIMAL(4, 2))