from abc import ABC, abstractmethod

class RegistryRouteBase(ABC):
    def __init__(self):
        self._router = list()

        self._storage_route()

    @abstractmethod
    def _storage_route(self):
        pass
    
    def get_router(self):
        return self._router