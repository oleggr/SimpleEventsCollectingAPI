from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.schema import metadata


class AbstractService:

    DB_FILENAME = 'database.db'
    conn_string = 'sqlite:///database.db'

    def __init__(self) -> None:
        self.engine = create_engine(self.conn_string, echo=True)

    async def execute(self, query):
        with self.engine.connect() as conn:
            result = conn.execute(query)
        return result

    async def insert(self, query) -> int:
        result = await self.execute(query)
        inserted_index = result.inserted_primary_key[0]
        return inserted_index

    async def select(self, query):
        with self.engine.connect() as conn:
            return conn.execute(query).fetchone()

    async def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    async def create_tables(self):
        metadata.create_all(self.engine)
