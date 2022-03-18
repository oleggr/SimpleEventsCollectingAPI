from datetime import datetime, date
from pydantic import BaseModel, validator


class UserBasic(BaseModel):
    balance: float = 0.0
    creation_date: date = 0
    age: int = 0
    city: str = ''
    last_activity: datetime = 0
    tariff: int = 0


class User(UserBasic):
    id: int

    @validator('id')
    def id_validation(cls, v: int):
        if not (v > 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v
