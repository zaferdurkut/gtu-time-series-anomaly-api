from src.infra.redis_adapter.cache_adapter import CacheAdapter
from src.infra.config.redis_adapter_config import get_redis_client
import redis


class RedisAdapter(CacheAdapter):
    def __init__(self):
        self.client = get_redis_client()

    def set(self, key, value, expires: int):
        result = self.client.set(key, value, ex=expires)
        return result

    def get(self, key):
        result = self.client.get(key)
        return result

    def exist(self, key):
        result = self.client.exists(key)
        return result

    def get_all_key(self):
        keys = []
        for key in self.client.scan_iter(match="*"):
            keys.append(key)

        return keys

    def delete_key(self, key):
        self.client.delete(key)

    @staticmethod
    def service_check():
        try:
            client = get_redis_client()
            result = client.ping()
            if result is True:
                return True
        except Exception as e:
            return False
        return False

if __name__ == '__main__':
    result = RedisAdapter.service_check()
    print(result)
