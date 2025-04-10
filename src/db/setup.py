from typing import TYPE_CHECKING, Type

from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from settings import get_settings

if TYPE_CHECKING:
    from db.base_model import Base


def build_sqlalchemy_plugin(base_model_class: Type["Base"]) -> SQLAlchemyPlugin:
    config = SQLAlchemyAsyncConfig(
        connection_string=get_settings().postgres_dsn,
        create_all=True,
        metadata=base_model_class.metadata,
    )
    return SQLAlchemyPlugin(config=config)
