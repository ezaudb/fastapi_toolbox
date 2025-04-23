from fastapi import FastAPI

from core.registry_route.registry_basic import RegistryBasic

class RegistryRoute:
    def __init__(self, app: FastAPI = None):
        self._app = app
        self._router = list()

        self._storage_route()

    def _storage_route(self):
        registry_basic = RegistryBasic()
        self._router.extend(registry_basic.get_router())

    def registry_all(self):
        if not self._app:
            raise Exception("Informe o App FastAPI")
        
        for item in self._router:
            self._app.include_router(item)

    def get_public_route(self):
        public_route_list = [item.routes[0].__dict__["path"] for item in self._router 
                              if "public" in item.routes[0].__dict__["tags"]]

        public_route_list.append("/docs")
        public_route_list.append("/openapi.json")
        
        return public_route_list                