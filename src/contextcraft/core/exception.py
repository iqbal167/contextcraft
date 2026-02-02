import logging

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("contextcraft.error")


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    logger.warning(
        "http exception",
        extra={
            "method": request.method,
            "url": str(request.url),
            "status_code": exc.status_code,
        },
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
            }
        },
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "unhandled exception",
        extra={
            "method": request.method,
            "url": str(request.url),
            "exception_type": type(exc).__name__,
        },
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL SERVER ERROR",
                "message": "Internal Server Error",
            }
        },
    )
