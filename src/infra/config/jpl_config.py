from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")


class JPLUrls:
    jpl_data_base = config('JPL_DATA_BASE')
    jpl_image_base = config('JPL_IMAGE_BASE')


columns = ["decimal_year",
           "east", "north", "vert",
           "e_sig", "n_sig", "v_sig",
           "e_cor", "n_cor", "v_cor",
           "J2000_seconds", "year", "month",
           "day", "hour", "minute", "second"
           ]
