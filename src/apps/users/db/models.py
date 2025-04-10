from datetime import datetime

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.base_model import Base
from utils.tzware_datetime import tzware_datetime


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=tzware_datetime
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=tzware_datetime, onupdate=tzware_datetime
    )
