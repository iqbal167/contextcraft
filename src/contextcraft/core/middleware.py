import logging
import time

from fastapi import Request

# Logger for request middleware. contextcraft.request is used to log request details.
logger = logging.getLogger("contextcraft.request")

EXCLUDE_PATHS = ["/docs", "/openapi.json", "/api/v1/healthz"]


async def request_logging_middleware(request: Request, call_next):
    if request.url.path in EXCLUDE_PATHS:
        return await call_next(request)

    # Use perf_counter for high precision timing
    start_time = time.perf_counter()
    response = await call_next(request)
    duration = (time.perf_counter() - start_time) * 1000

    logger.info(
        "request completed",
        extra={
            "method": request.method,
            "url": str(request.url),
            "status_code": response.status_code,
            "duration_ms": round(duration, 2),
        },
    )

    return response
