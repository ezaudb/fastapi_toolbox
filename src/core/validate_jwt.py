from fastapi import Request, status
from fastapi.responses import JSONResponse

from classe.my_jwt import MyJwt
from core.registry_route.registry_route import RegistryRoute

ROTA_PUBLICA = ["/auth/login"]

async def autenticate(request: Request, call_next):
    registry_route = RegistryRoute()
    if request.url.path in registry_route.get_public_route():
        return await call_next(request)

    request_authorization = request.headers.get("Authorization")
    
    if (not request_authorization) or (not request_authorization.startswith("Bearer ")):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Token de Autenticação Não Fornecido ou Inválido")
    
    token = request_authorization.split()[1]
    try:
        my_jwt = MyJwt()
        my_jwt.decode(token)
    except:
       return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Falha na autenticação: verifique seu token de acesso")

    return await call_next(request)        