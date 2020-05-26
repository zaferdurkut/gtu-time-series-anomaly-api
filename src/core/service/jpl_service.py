from datetime import datetime

from fastapi import Depends

from src.infra.client.jpl.jpl import JPLClient
from src.core.model.anomaly_dto import *
import numpy as np


class JPLService():
    def __init__(self, jpl_client: JPLClient = Depends(JPLClient)):
        self.jpl_client = jpl_client

    def get_anomaly_data(self, data_name: str, window_range_by_day: int, sigma_count: int):
        base_data = self.jpl_client.get_data(data_name=data_name)
        if base_data is None:
            return None
        base_data = self.__update_base_data(base_data=base_data)
        day_step_by_year = self.__day_to_year(day=window_range_by_day)

        year_range = self.__set_range(base_data, day_step_by_year)
        general_items = GeneralAnomalyTotalModel.to_model(window_range=window_range_by_day,
                                                          sigma_count=sigma_count,
                                                          east_items=[],
                                                          north_items=[],
                                                          vert_items=[]
                                                          )

        for year_item in year_range - 1:  # for last item
            mask = (base_data.decimal_year >= year_item) & (base_data.decimal_year <= year_item + 1)
            mask_frame = base_data.loc[mask]

            if mask_frame["east"].shape[0] > 1:
                std_east, std_north, std_vert = self.__get_std_for_mask(mask_frame=mask_frame, sigma_count=sigma_count)
                mean_east, mean_north, mean_vert = self.__get_mean_for_mask(mask_frame=mask_frame)

                east_items = self.__get_east_anomaly_data(window_start=year_item,
                                                          window_end=year_item + 1,
                                                          mask_frame=mask_frame,
                                                          mean_east=mean_east,
                                                          std_east=std_east)

                north_items = self.__get_north_anomaly_data(window_start=year_item,
                                                            window_end=year_item + 1,
                                                            mask_frame=mask_frame,
                                                            mean_north=mean_north,
                                                            std_north=std_north)

                vert_items = self.__get_vert_anomaly_data(window_start=year_item,
                                                                 window_end=year_item + 1,
                                                                 mask_frame=mask_frame,
                                                                 mean_vert=mean_vert,
                                                                 std_vert=std_vert)
                general_items.east_items.append(east_items)
                general_items.north_items.append(north_items)
                general_items.vert_items.append(vert_items)

        return general_items

    def __get_east_anomaly_data(self, window_start, window_end, mask_frame, mean_east, std_east):
        mask = (mask_frame.east < mean_east - std_east) | (mask_frame.east > mean_east + std_east)
        mask_frame = mask_frame.loc[mask]

        east_items = EastAnomalyTotalModel.to_model(window_start=window_start,
                                                    window_end=window_end,
                                                    mean=mean_east,
                                                    std=std_east,
                                                    items=[]
                                                    )
        for index, row in mask_frame.iterrows():
            east_item = EastAnomalyItemModel.to_model(decimal_year=row.decimal_year, value=row.east)
            east_items.items.append(east_item)

        return east_items

    def __get_north_anomaly_data(self, window_start, window_end, mask_frame, mean_north, std_north):
        mask = (mask_frame.east < mean_north - std_north) | (mask_frame.east > mean_north + std_north)
        mask_frame = mask_frame.loc[mask]

        north_items = EastAnomalyTotalModel.to_model(window_start=window_start,
                                                     window_end=window_end,
                                                     mean=mean_north,
                                                     std=std_north,
                                                     items=[]
                                                     )
        for index, row in mask_frame.iterrows():
            north_item = EastAnomalyItemModel.to_model(decimal_year=row.decimal_year, value=row.east)
            north_items.items.append(north_item)

        return north_items

    def __get_vert_anomaly_data(self, window_start, window_end, mask_frame, mean_vert, std_vert):
        mask = (mask_frame.east < mean_vert - std_vert) | (mask_frame.east > mean_vert + std_vert)
        mask_frame = mask_frame.loc[mask]

        vert_items = EastAnomalyTotalModel.to_model(window_start=window_start,
                                                     window_end=window_end,
                                                     mean=mean_vert,
                                                     std=std_vert,
                                                     items=[]
                                                     )
        for index, row in mask_frame.iterrows():
            vert_item = EastAnomalyItemModel.to_model(decimal_year=row.decimal_year, value=row.east)
            vert_items.items.append(vert_item)

        return vert_items

    def __get_std_for_mask(self, mask_frame, sigma_count):
        std_mask_frame = mask_frame.std(skipna=True) * sigma_count
        std_east, std_north, std_vert = std_mask_frame.east, std_mask_frame.north, std_mask_frame.vert
        return std_east, std_north, std_vert

    def __get_mean_for_mask(self, mask_frame):
        mean_mask_frame = mask_frame.mean(skipna=True)
        mean_east, mean_north, mean_vert = mean_mask_frame.east, mean_mask_frame.north, mean_mask_frame.vert
        return mean_east, mean_north, mean_vert

    def __day_to_year(self, day: float) -> float:
        return day / 365.6

    def __update_base_data(self, base_data):
        base_data.decimal_year = base_data.decimal_year.astype(float)
        base_data.east = base_data.east.astype(float)
        base_data.north = base_data.north.astype(float)
        base_data.vert = base_data.vert.astype(float)

        return base_data

    def __set_range(self, base_data, day_step_by_year):
        data_start_date = base_data.iloc[[0, -1]].iloc[0].decimal_year
        data_end_date = base_data.iloc[[0, -1]].iloc[1].decimal_year
        year_range = np.arange(data_start_date, data_end_date, day_step_by_year)
        year_range[-1] = data_end_date if year_range[-1] <= data_end_date else year_range[-1]
        return year_range


if __name__ == '__main__':
    result = JPLService(jpl_client=JPLClient).get_anomaly_data(data_name="ATW2", window_range_by_day=100, sigma_count=3)

    print(result)
