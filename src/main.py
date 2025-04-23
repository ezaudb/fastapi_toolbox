from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from core.validate_jwt import autenticate

from core.registry_route.registry_route import RegistryRoute

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.middleware("http")(autenticate)

registry_route = RegistryRoute(app)
registry_route.registry_all()