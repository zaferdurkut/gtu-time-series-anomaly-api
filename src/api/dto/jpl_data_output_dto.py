from typing import List

from pydantic import BaseModel, Field


class JPLDataOutputModel(BaseModel):
    items: List[dict] = Field(...)

    @staticmethod
    def to_model(items: dict):
        return JPLDataOutputModel(items=items)
