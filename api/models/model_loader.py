from . import dish, dish_ingredient, order, order_detail, order_item, feedback, payment, promotion, used_promotion

from ..dependencies.database import engine


def index():
    order.Base.metadata.create_all(engine)
    order_detail.Base.metadata.create_all(engine)
    order_item.Base.metadata.create_all(engine)
    dish.Base.metadata.create_all(engine)
    dish_ingredient.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    used_promotion.Base.metadata.create_all(engine)
