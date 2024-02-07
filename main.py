from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from debug_toolbar.middleware import DebugToolbarMiddleware
from app.middlewares.cors import origins
from app.middlewares.exception import ExceptionHandlerMiddleware

from app.api import category, user, campaign, cart, product, order, review

app = FastAPI()
app.add_middleware(ExceptionHandlerMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    DebugToolbarMiddleware,
    panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
)

app.include_router(category.router, prefix="/categories", tags=["Category"])
app.include_router(user.router, prefix="/users", tags=["User"])
app.include_router(campaign.router, prefix="/campaigns", tags=["Campaign"])
app.include_router(product.router, prefix="/products", tags=["Product"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(order.router, prefix="/order", tags=["Order"])
app.include_router(review.router, prefix="/review", tags=["Review"])
