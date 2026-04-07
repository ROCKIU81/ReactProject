from app.database.connector import PostgreDB
import logging

class DBFunction:
    def __init__(self,config):
        self.db=PostgreDB(config)
        self.config=config

    async def get_data(self,table_name,id):
        sql_command=f'''select read_record($1,$2) '''

        args=table_name,id
        if not self.db.pool:
            await self.db.create_pool()

            try:
                async with self.db.pool.acquire() as conn:
                    data=await conn.fetch(sql_command,*args)
                return data

            except Exception as e:
                logging.error(f"error:+{str(e)}")

    async def set_data(self,table_name,columns,values):
        sql_command=f'''select create_record($1,$2,$3) '''

        args=table_name,columns,values
        if not self.db.pool:
            await self.db.create_pool()
            try:
                async with self.db.pool.acquire() as conn:
                    res=await conn.execute(sql_command,*args)
                return logging.info(f"Данные занесены в таблицу. ID:{res}")
            except Exception as e:
                logging.error(f"error:{str(e)}")


    async def delete_data(self,table_name,id):
        sql_command=f'''select delete_record($1,$2) '''

        args=table_name,id
        if not self.db.pool:
            await self.db.create_pool()
            try:
                async with self.db.pool.acquire() as conn:
                    await conn.execute(sql_command,*args)
                return logging.info("Данные удалены")
            except Exception as e:
                logging.error(f"error:{str(e)}")

    async def update_data(self,table_name,id,columns,values):
        sql_command=f'''select update_record($1,$2,$3,$4) '''

        args=table_name,id,columns,values
        if not self.db.pool:
            await self.db.create_pool()
            try:
                async with self.db.pool.acquire() as conn:
                    res=await conn.execute(sql_command,*args)
                return logging.info(f"Данные обновлены: {str(res)}")
            except Exception as e:
                logging.error(f"error:{str(e)}")



            
        