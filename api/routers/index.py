from . import (dish, orders, order_details, dish_ingredients, feedback, order_items, payments, promotion,
               used_promotion)


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(dish_ingredients.router)
    app.include_router(dish.router)
    app.include_router(feedback.router)
    app.include_router(order_items.router)
    app.include_router(payments.router)
    app.include_router(promotion.router)
    app.include_router(used_promotion.router)
