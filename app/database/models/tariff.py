from datetime import date
from pydantic import BaseModel, validator


class TariffBasic(BaseModel):
    name: str = ''
    start_date: date = 0
    end_date: date = 0
    minutes: int = 0
    sms: int = 0
    traffic: int = 0


class Tariff(TariffBasic):
    id: int

    @validator('id')
    def courier_id_validation(cls, v: int):
        if not (v > 0 and isinstance(v, int)):
            raise ValueError('Id must be positive integer')
        return v
