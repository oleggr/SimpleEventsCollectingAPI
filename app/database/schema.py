from sqlalchemy import (
    Column, Integer, Float, Date, DateTime,
    MetaData, String, Table,
)


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(column_0_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('balance', Float),
    Column('creation_date', Date),
    Column('age', Integer),
    Column('city', String),
    Column('last_activity', DateTime),
    Column('tariff', Integer),
)

tariff_table = Table(
    'tariffs',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('start_date', Date),
    Column('end_date', Date),
    Column('minutes', Integer),
    Column('sms', Integer),
    Column('traffic', Integer),
)
