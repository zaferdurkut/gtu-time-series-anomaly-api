import os
from fastapi import APIRouter

from src.api.dto.heartbeat_output_dto import HeartbeatOutputModel
from src.api.dto.service_check_output_dto import ServiceCheckOutputModel
from src.infra.redis_adapter.redis_adapter import RedisAdapter

router = APIRouter()


@router.get("/heartbeat", response_model=HeartbeatOutputModel, status_code=200)
def heartbeat():
    return HeartbeatOutputModel.to_model(os.environ['HOSTNAME'])


@router.get("/service-check", response_model=ServiceCheckOutputModel, status_code=200)
def service_check():
    return ServiceCheckOutputModel.to_model(
        redis_cache_check=RedisAdapter.service_check()
    )
