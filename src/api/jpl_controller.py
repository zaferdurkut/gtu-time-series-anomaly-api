import ast
import json
import os
import tempfile

from fastapi import APIRouter, Response
from starlette.responses import StreamingResponse, FileResponse

from src.api.dto.jpl_all_list_output_dto import JPLAllListOutputModel
from src.api.dto.jpl_data_output_dto import JPLDataOutputModel
from src.core.service.jpl_service import JPLService
from src.infra.client.jpl.jpl import JPLClient
from src.core.model.anomaly_dto import GeneralAnomalyTotalModel

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

    @param data_name: name of the jpl data \t

    @return: JPLDataOutputModel
    """
    result = JPLClient.get_data(data_name=data_name)
    if result is not None:
        results = result.to_dict(orient='records')
        return JPLDataOutputModel(items=results)
    else:
        return JPLDataOutputModel(items=[])


@router.get("/anomaly-data", response_model=GeneralAnomalyTotalModel, status_code=200)
def get_base_data(data_name: str, window_range_by_day: int, sigma_count: int):
    """
    This method returns a data of analysis jbl results and a list of anomaly data
    https://sideshow.jpl.nasa.gov/pub/JPL_GPS_Timeseries/repro2018a/post/point/AB27.series

    @param data_name: name of the jpl data \t
    @param window_range_by_day: time interval to look \t
    @param sigma_count: tolerance range for standart deviation \t

    @return: GeneralAnomalyTotalModel
    """
    result = JPLService(jpl_client=JPLClient).get_anomaly_data(data_name=data_name,
                                         window_range_by_day=window_range_by_day,
                                         sigma_count = sigma_count
                                         )
    if result is not None:
        return result
    else:
        return GeneralAnomalyTotalModel.to_model(window_range=window_range_by_day,
                                                 sigma_count=sigma_count,
                                                 east_items=[],
                                                 north_items=[],
                                                 vert_items=[]
                                                 )
