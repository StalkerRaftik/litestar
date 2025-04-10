from typing import Optional

import msgspec


class UpdateUserDTO(msgspec.Struct):
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None
