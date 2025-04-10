from litestar import Router

from apps.users.api.controllers.user_controller import UserController


def create_user_router() -> Router:
    return Router(
        path="/users",
        tags=["users"],
        route_handlers=[
            UserController,
        ],
    )
