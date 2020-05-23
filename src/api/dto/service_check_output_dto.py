from pydantic import BaseModel, Field


class ServiceCheckOutputModel(BaseModel):
    redis_cache_check: bool = Field(...)

    @staticmethod
    def to_model(redis_cache_check: bool):
        return ServiceCheckOutputModel(
            redis_cache_check=redis_cache_check)
