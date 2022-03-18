from datetime import datetime

from app.database.schema import users_table
from app.database.db_handler import DBHandler
from app.database.models.user import UserBasic, User


class UserService:

    def __init__(self):
        self.db = DBHandler()

    async def add_user(self, user: UserBasic) -> [int, bool]:
        user.last_activity = datetime.now()

        user_id = await self.db.insert(
            users_table.insert().values({
                'balance': user.balance,
                'creation_date': user.creation_date,
                'age': user.age,
                'city': user.city,
                'last_activity': user.last_activity,
                'tariff': user.tariff,
            })
        )

        return user_id if user_id else False

    async def get_user(self, user_id: int) -> [User, bool]:
        user_row = await self.db.select(
            users_table.select().where(
                users_table.c.id == user_id,
            )
        )

        if user_row:
            return User(**user_row)
        else:
            return False

    async def update_user(self, user_id: int, data: dict) -> bool:
        user = await self.get_user(user_id)
        if not user:
            return False

        data['last_activity'] = datetime.now()

        await self.db.execute(
            users_table.update()
            .where(users_table.c.id == user_id)
            .values(data)
        )
        return True

    async def delete_user(self, user_id: int) -> bool:
        await self.db.execute(
            users_table.delete().where(
                users_table.c.id == user_id,
            )
        )

        user = await self.get_user(user_id)
        return False if user else True

    def sync_get_user(self, user_id):
        user_row = self.db.sync_select(
            users_table.select().where(
                users_table.c.id == user_id,
            )
        )

        if user_row:
            return User(**user_row)
        else:
            return False
