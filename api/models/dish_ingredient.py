from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class DishIngredient(Base):
    __tablename__ = "dish_ingredients"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    ingredient_name = Column(String(255))
    ingredient_description = Column(String(255))
    serving_size = Column(Integer)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)