import asyncio
import json

import aiohttp
from pydantic import BaseModel


class CurrentValueModel(BaseModel):
    status: int
    message: str
    data: dict = {}


LINK = "https://currate.ru/api/"


class CurrateApi:
    def __init__(self, token: str) -> None:
        self.token = token

    async def get_value(self, currency: str) -> CurrentValueModel:
        params = {
            "get": "rates",
            "pairs": currency,
            "key": self.token,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(LINK, params=params) as response:
                data = await response.text()
                data_json = json.loads(data)

                return CurrentValueModel(**data_json)
