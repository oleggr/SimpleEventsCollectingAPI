from app.database.schema import tariff_table
from app.database.models.tariff import TariffBasic, Tariff
from app.database.db_handler import DBHandler


class TariffService:

    def __init__(self):
        self.db = DBHandler()

    async def add_tariff(self, tariff: TariffBasic) -> [int, bool]:
        tariff_id = await self.db.insert(
            tariff_table.insert().values({
                'name': tariff.name,
                'start_date': tariff.start_date,
                'end_date': tariff.end_date,
                'minutes': tariff.minutes,
                'sms': tariff.sms,
                'traffic': tariff.traffic,
            })
        )

        return tariff_id if tariff_id else False

    async def get_tariff(self, tariff_id: int) -> [Tariff, bool]:
        user_row = await self.db.select(
            tariff_table.select().where(
                tariff_table.c.id == tariff_id,
            )
        )

        if user_row:
            return Tariff(**user_row)
        else:
            return False

    async def update_tariff(self, tariff_id: int, data: dict) -> bool:
        tariff = await self.get_tariff(tariff_id)
        if not tariff:
            return False

        await self.db.execute(
            tariff_table.update()
            .where(tariff_table.c.id == tariff_id)
            .values(data)
        )
        return True

    async def delete_tariff(self, tariff_id: int) -> bool:
        await self.db.execute(
            tariff_table.delete().where(
                tariff_table.c.id == tariff_id,
            )
        )

        user = await self.get_tariff(tariff_id)
        return False if user else True
