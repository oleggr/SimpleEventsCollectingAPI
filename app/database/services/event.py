from app.database.schema import events_table
from app.database.db_handler import DBHandler
from app.database.models.event import EventBasic, Event
from app.database.services.user import UserService


class EventService:

    def __init__(self):
        self.db = DBHandler()

    async def add_event(self, event: EventBasic) -> [int, bool]:
        user = UserService().sync_get_user(event.id_user)
        if not user:
            return False

        event_id = await self.db.insert(
            events_table.insert().values({
                'time': event.time,
                'id_user': event.id_user,
                'service_type': event.service_type,
                'volume': event.volume,
            })
        )

        return event_id if event_id else False

    async def get_event(self, event_id: int) -> [Event, bool]:
        event_row = await self.db.select(
            events_table.select().where(
                events_table.c.id == event_id,
            )
        )

        if event_row:
            return Event(**event_row)
        else:
            return False

    async def update_event(self, event_id: int, data: dict) -> bool:
        event = await self.get_event(event_id)
        if not event:
            return False

        await self.db.execute(
            events_table.update()
            .where(events_table.c.id == event_id)
            .values(data)
        )
        return True

    async def delete_event(self, event_id: int) -> bool:
        await self.db.execute(
            events_table.delete().where(
                events_table.c.id == event_id,
            )
        )

        event = await self.get_event(event_id)
        return False if event else True
