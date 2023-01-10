from fastapi import APIRouter, Depends

from src.schemas import Result
from src.service import CurrencyExchangeService

router_rates = APIRouter(prefix="/rates", tags=['Currency exchange'])


@router_rates.get("/", response_model=Result)
async def get(
        from_s: str = "USD",
        to: str = "RUB",
        value: int = 1,
        service: CurrencyExchangeService = Depends()
) -> Result:
    return await service.get(f"{from_s}{to}", value)
