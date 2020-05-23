from src.infra.redis_adapter.redis_adapter import RedisAdapter
import json
from functools import wraps

redis = RedisAdapter()

def cached(func):
    """
    Decorator that caches the results of the function call.

    We use Redis in this example, but any cache (e.g. memcached) will work.
    We also assume that the result of the function can be seralized as JSON,
    which obviously will be untrue in many situations. Tweak as needed.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Generate the cache key from the function's arguments.
        key_parts = [func.__name__] + list(args)
        key = '-'.join(key_parts)
        result = redis.get(key)

        if result is None:
            # Run the function and cache the result for next time.
            value = func(*args, **kwargs)
            value_json = json.dumps(value)
            redis.set(key, value_json)
        else:
            # Skip the function entirely and use the cached value instead.
            value_json = result.decode('utf-8')
            value = json.loads(value_json)

        return value

    return wrapper
