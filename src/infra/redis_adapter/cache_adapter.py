from abc import ABC, abstractmethod


class CacheAdapter(ABC):
    @abstractmethod
    def set(self, key, value, expires: int):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def exist(self, key):
        pass

    @abstractmethod
    def get_all_key(self):
        pass

    @abstractmethod
    def delete_key(self, key):
        pass
