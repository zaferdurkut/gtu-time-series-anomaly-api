import os
from fastapi import APIRouter

from src.api.dto.jpl_all_list_dto import JPLAllListOutputModel
from src.infra.client.jpl.jpl import JPLClient

router = APIRouter()


@router.get("/all", response_model=JPLAllListOutputModel, status_code=200)
def get_all_items():
    """
    This method returns a list of all items from
    https://sideshow.jpl.nasa.gov/pub/JPL_GPS_Timeseries/repro2018a/post/point/
    @return: JPLAllListOutputModel
    """
    result = JPLClient.get_all_list()
    return JPLAllListOutputModel(items=result)
