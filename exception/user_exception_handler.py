from fastapi import Request
from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def http_exception(request:Request, exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )