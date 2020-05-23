from pydantic import BaseModel, Field


class HeartbeatOutputModel(BaseModel):
    host_name: str = Field(...)

    @staticmethod
    def to_model(host_name: str):
        return HeartbeatOutputModel(host_name=host_name)
