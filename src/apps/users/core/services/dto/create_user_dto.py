import msgspec


class CreateUserDTO(msgspec.Struct):
    name: str
    surname: str
    password: str
