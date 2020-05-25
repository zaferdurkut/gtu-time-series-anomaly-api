import json
import requests
from firefly_logger.log_provider import logger
from requests import Response
from starlette import status
from bs4 import BeautifulSoup

from src.infra.client.jpl.dto.jpl_list_dto import JPLListResponseModel
from src.infra.config.jpl_config import JPLUrls
from src.infra.config.redis_adapter_config import get_redis_client, DEFAULT_TTL_DURATION_IN_MINUTES
from src.infra.redis_adapter.redis_adapter import RedisAdapter

redis_client = RedisAdapter()


class JPLClient:

    @staticmethod
    def get_all_list():
        if redis_client.exist(key="get_all_list_from_jpl"):
            return json.loads(redis_client.get(key="get_all_list_from_jpl"))

        response = requests.get(JPLUrls.jpl_data_base)
        result = build_all_list_result(response)

        redis_client.set(key="get_all_list_from_jpl",
                              value=json.dumps(result, default=dict), expires=DEFAULT_TTL_DURATION_IN_MINUTES)

        return result


def build_all_list_result(response: Response) -> list:
    if response.status_code == status.HTTP_200_OK:
        soup = BeautifulSoup(response.text, 'html.parser')

        result = []
        for tag in soup.findAll("a"):
            try:
                href = tag.get('href')
                name, path = href.split(".")
                result.append(JPLListResponseModel.to_model(name=name, href=JPLUrls.jpl_data_base + href))
            except AttributeError as ae:
                pass
            except ValueError as ve:
                pass

        return result
    else:
        logger.error("JPL returns error: {}".format(response.text))
        raise Exception(response.text)


if __name__ == '__main__':
    result = JPLClient.get_all_list()

    print(result)
