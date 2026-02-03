import logging

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("contextcraft.error")


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    correlation_id = getattr(request.state, "correlation_id", "unknown")

    logger.warning(
        "http exception",
        extra={
            "correlation_id": correlation_id,
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
        headers={"X-Correlation-ID": correlation_id},
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):
    correlation_id = getattr(request.state, "correlation_id", "unknown")

    logger.exception(
        "unhandled exception",
        extra={
            "correlation_id": correlation_id,
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
        headers={"X-Correlation-ID": correlation_id},
    )
