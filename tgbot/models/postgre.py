import asyncpg
from asyncpg.pool import Pool
from typing import Union
from tgbot.config import load_config
from asyncpg import Connection


class DataBase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        config = load_config(".env")
        self.pool = await asyncpg.create_pool(
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            database=config.db.database,
        )

    # async def execute(
    #     self,
    #     command,
    #     *args,
    #     fetch: bool = False,
    #     fetchval: bool = False,
    #     fetchrow: bool = False,
    #     execute: bool = False,
    # ):
    #     async with self.pool.acquire() as connection:
    #         connection: Connection
    #         async with connection.transaction():
    #             if fetch:
    #                 result = await connection.fetch(command, *args)
    #             elif fetchval:
    #                 result = await connection.fetchval(command, *args)
    #             elif fetchrow:
    #                 result = await connection.fetchrow(command, *args)
    #             elif execute:
    #                 result = await connection.execute(command, *args)
    #             else:
    #                 result = None
    #         return result
    #
    # async def create_table_stocks(self):
    #     create_tab = """
    #     CREATE TABLE IF NOT EXISTS Stocks_tab(
    #     id SERIAL PRIMARY KEY,
    #     stock_name VARCHAR(255) NOT NULL,
    #     stock_description TEXT NOT NULL,
    #     stock_img TEXT NOT NULL
    #     );
    #     """
    #     await self.execute(create_tab, execute=True)
    #
    # async def add_stock(self, id, stock_name, stock_description, stock_img):
    #     sql = "INSERT INTO Stocks_tab('id', 'stock_name', 'stock_description', 'stock_img') VALUES($1, $2, $3)"
    #     return await self.execute(
    #         sql, stock_name, stock_description, stock_img, fetchrow=True
    #     )
    #
    # async def select_all_stocks(self):
    #     select_stocks = "SELECT * FROM Stocks_tab"
    #     return await self.execute(select_stocks, fetch=True)
    #
    # @staticmethod
    # def format_args(sql, parameters: dict):
    #     sql += " AND ".join(
    #         [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
    #     )
    #     return sql, tuple(parameters.values())
    #
    # async def select_stock(self, **kwargs):
    #     select_stock = "SELECT * FROM Stocks_tab WHERE stock_name=$1"
    #     select_stock, parameters = self.format_args(select_stock, parameters=kwargs)
    #     return await self.execute(select_stock, *parameters, fetchrow=True)
    #
    # async def delete_stocks(self):
    #     await self.execute("DELETE FROM Stocks_tab WHERE TRUE", execute=True)
    #
    # async def delete_stock(self, **kwargs):
    #     if "stock_name" in kwargs:
    #         delete = "DELETE FROM Stocks_tab WHERE stock_name=$1"
    #         await self.execute(delete, fetchrow=True)
