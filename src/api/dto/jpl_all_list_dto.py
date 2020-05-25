from typing import List

from pydantic import BaseModel, Field


class JPLAllListOutputModel(BaseModel):
    items: List[dict] = Field(...)

    @staticmethod
    def to_model(items: dict):
        return JPLAllListOutputModel(items=items)
