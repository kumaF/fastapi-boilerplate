from fastapi.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_204_NO_CONTENT


async def http_exception_handler(request: Request, e: HTTPException):
    if e.status_code == HTTP_204_NO_CONTENT:
        return Response(status_code=e.status_code)

    return JSONResponse(
        status_code=e.status_code,
        content={
            "success": False,
            "detail": e.detail
        }
    )
