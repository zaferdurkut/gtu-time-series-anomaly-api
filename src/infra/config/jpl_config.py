from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")


class JPLUrls:
    jpl_data_base = config('JPL_DATA_BASE')
    jpl_image_base = config('JPL_IMAGE_BASE')
