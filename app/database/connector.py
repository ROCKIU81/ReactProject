import asyncpg
from app.utils.logger import set_log
import logging

set_log()

class PostgreDB:
    def __init__(self,config):
        self.pool=None
        self.db_name=config.DBNAME
        self.user_db=config.USER
        self.pass_db=config.PASSWORD
        self.host_db=config.HOST
        self.port_db=config.PORT

    async def create_pool(self):

        self.pool= await asyncpg.create_pool(database=self.db_name,user=self.user_db,password=self.pass_db,host=self.host_db,port=self.port_db)
        logging.info("Пул создан")