from pydantic import BaseModel, Field
from typing import List


class JPLListResponseModel(BaseModel):
    name: str = Field(None)
    href: str = Field(None)

    @staticmethod
    def to_model(name, href):
        return JPLListResponseModel(name=name, href=href)
