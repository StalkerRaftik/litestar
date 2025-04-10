from datetime import datetime

import msgspec


class User(msgspec.Struct):
    id: int
    name: str
    surname: str
    password: str
    created_at: datetime
    updated_at: datetime
