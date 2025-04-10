from datetime import datetime

import msgspec


class ReturnUserDTO(msgspec.Struct):
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime
