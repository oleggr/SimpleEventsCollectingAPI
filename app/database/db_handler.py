from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.schema import metadata


class DBHandler:

    DB_FILENAME = 'database.db'
    conn_string = 'sqlite:///%s'

    def __init__(self, db_file=None) -> None:
        if db_file:
            self.DB_FILENAME = db_file

        self.conn_string = self.conn_string % self.DB_FILENAME
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

    def create_tables(self):
        metadata.create_all(self.engine)
