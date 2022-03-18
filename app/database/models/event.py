from datetime import date
from pydantic import BaseModel, validator


class EventBasic(BaseModel):
    time: date = 0
    id_user: int = 0
    service_type: int = 0
    volume: int = 0

    # Too cool validation. Needed to adapted for using with tests.
    # @validator('id_user')
    # def user_id_validation(cls, v: int):
    #     user = UserService().sync_get_user(v)
    #     if not user:
    #         raise ValueError('User not exist')


class Event(EventBasic):
    id: int

    @validator('id')
    def id_validation(cls, v: int):
        if not (v > 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v
