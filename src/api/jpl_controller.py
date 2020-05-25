import ast
import json
import os
import tempfile

from fastapi import APIRouter, Response
from starlette.responses import StreamingResponse, FileResponse

from src.api.dto.jpl_all_list_dto import JPLAllListOutputModel
from src.api.dto.jpl_data_dto import JPLDataOutputModel
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

@router.get("/base-data", response_model=JPLDataOutputModel, status_code=200)
def get_base_data(data_name):
    """
    This method returns a data of series jbl
    https://sideshow.jpl.nasa.gov/pub/JPL_GPS_Timeseries/repro2018a/post/point/AB27.series
    @return: JPLDataOutputModel
    """
    result = JPLClient.get_data(data_name=data_name)
    if result is not None:
        results = result.to_dict(orient='records')
        return JPLDataOutputModel(items=results)
    else:
        return JPLDataOutputModel(items=[])
