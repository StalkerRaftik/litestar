from litestar import Litestar, Router

from apps.users.api.router import create_user_router
from db.base_model import Base as base_model_class
from db.models import *
from db.setup import build_sqlalchemy_plugin
from settings import get_settings


def create_app() -> Litestar:
    settings = get_settings()
    return Litestar(
        route_handlers=[
            Router(
                path="/api",
                route_handlers=[
                    create_user_router(),
                ],
            ),
        ],
        plugins=[
            build_sqlalchemy_plugin(base_model_class),
        ],
        debug=settings.DEBUG,
    )


app = create_app()
