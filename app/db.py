# Setting up the DB connection

from psycopg_pool import ConnectionPool
from app.settings import settings

pool = ConnectionPool(
    setting.database_url,
    min_size=1,
    max_size=settings.datavase_pool_size,
)