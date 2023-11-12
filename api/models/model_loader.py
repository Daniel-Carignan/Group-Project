from . import orders, order_details, dishes, order_items, dish_ingredients, feedback, payments, promotions, used_promotions

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    dishes.Base.metadata.create_all(engine)
    dish_ingredients.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    used_promotions.Base.metadata.create_all(engine)
