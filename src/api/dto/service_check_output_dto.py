from pydantic import BaseModel, Field


class ServiceCheckOutputModel(BaseModel):
    big_query_check: bool = Field(...)
    redis_cache_check: bool = Field(...)
    db_connection_check: bool = Field(...)

    @staticmethod
    def to_model(big_query_check: bool, redis_cache_check: bool, db_connection_check: bool):
        return ServiceCheckOutputModel(
            big_query_check=big_query_check,
            redis_cache_check=redis_cache_check,
            db_connection_check=db_connection_check)
