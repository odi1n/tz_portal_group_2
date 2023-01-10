from fastapi import HTTPException

from src.schemas import Result
from src.settings import setting
from src.utils.currate_api import CurrateApi


class CurrencyExchangeService:
    async def get(self, currency, value) -> Result:
        get_value = await CurrateApi(setting.currate_api_key).get_value(currency=currency)
        current_value = get_value.data.get(currency)

        if current_value is None:
            raise HTTPException(status_code=404, detail="Error value currency")

        current = float(current_value) * value
        return Result(result=float("{0:.4f}".format(current)))
