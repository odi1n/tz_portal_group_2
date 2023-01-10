from fastapi import APIRouter

from .rates import router_rates

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(router_rates)
