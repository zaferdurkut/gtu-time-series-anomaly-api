from dotenv import load_dotenv
from starlette.config import Config
import redis

load_dotenv()

config = Config(".env")

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_DB = config('REDIS_DB')


def get_redis_client():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=int(REDIS_DB))
    return client
