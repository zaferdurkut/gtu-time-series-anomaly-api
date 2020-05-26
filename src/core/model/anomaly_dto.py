from typing import List

from pydantic import BaseModel, Field


class EastAnomalyItemModel(BaseModel):
    decimal_year: float = 0.0
    value: float = 0.0

    @staticmethod
    def to_model(decimal_year: float, value: float):
        return EastAnomalyItemModel(decimal_year=decimal_year, value=value)


class EastAnomalyTotalModel(BaseModel):
    window_start: float = 0.0
    window_end: float = 0.0
    mean: float = 0.0
    std: float = 0.0
    items: List[EastAnomalyItemModel] = []

    @staticmethod
    def to_model(window_start: float, window_end: float, mean: float, std: float, items: list):
        return EastAnomalyTotalModel(window_start=window_start,
                                     window_end=window_end,
                                     mean=mean,
                                     std=std,
                                     items=items)


class NorthAnomalyItemModel(BaseModel):
    decimal_year: float = 0.0
    value: float = 0.0

    @staticmethod
    def to_model(decimal_year: float, value: float):
        return NorthAnomalyItemModel(decimal_year=decimal_year, value=value)


class NortAnomalyTotalModel(BaseModel):
    window_start: float = 0.0
    window_end: float = 0.0
    mean: float = 0.0
    std: float = 0.0
    items: List[NorthAnomalyItemModel] = []

    @staticmethod
    def to_model(window_start: float, window_end: float, mean: float, std: float, items: list):
        return NortAnomalyTotalModel(window_start=window_start,
                                     window_end=window_end,
                                     mean=mean,
                                     std=std,
                                     items=items)


class VertAnomalyItemModel(BaseModel):
    decimal_year: float = 0.0
    value: float = 0.0

    @staticmethod
    def to_model(decimal_year: float, value: float):
        return VertAnomalyItemModel(decimal_year=decimal_year, value=value)


class VertAnomalyTotalModel(BaseModel):
    window_start: float = 0.0
    window_end: float = 0.0
    mean: float = 0.0
    std: float = 0.0
    items: List[VertAnomalyItemModel] = []

    @staticmethod
    def to_model(window_start: float, window_end: float, mean: float, std: float, items: list):
        return VertAnomalyTotalModel(window_start=window_start,
                                     window_end=window_end,
                                     mean=mean,
                                     std=std,
                                     items=items)


class GeneralAnomalyTotalModel(BaseModel):
    window_range: int = 0
    sigma_count: int = 0
    east_items: List[EastAnomalyTotalModel] = []
    north_items: List[NortAnomalyTotalModel] = []
    vert_items: List[VertAnomalyTotalModel] = []

    @staticmethod
    def to_model(window_range: int, sigma_count: int, east_items: list, north_items: list, vert_items: list):
        return GeneralAnomalyTotalModel(window_range=window_range,
                                        sigma_count=sigma_count,
                                        east_items=east_items,
                                        north_items=north_items,
                                        vert_items=vert_items)
