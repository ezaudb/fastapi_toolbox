from core.registry_route.base.registry_route_base import RegistryRouteBase
from route.auth import login
from route.home import welcome

class RegistryBasic(RegistryRouteBase):
    def _storage_route(self):
        self._router.append(login.router)
        self._router.append(welcome.router)