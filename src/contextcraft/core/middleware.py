import logging
import time
import uuid

from fastapi import Request

# Logger for request middleware. contextcraft.request is used to log request details.
logger = logging.getLogger("contextcraft.request")

EXCLUDE_PATHS = {"/docs", "/openapi.json", "/api/v1/healthz"}


async def request_logging_middleware(request: Request, call_next):
    if request.url.path in EXCLUDE_PATHS:
        return await call_next(request)

    start_time = time.perf_counter()
    # default: assume server error
    status_code = 500

    correlation_id = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    request.state.correlation_id = correlation_id

    try:
        response = await call_next(request)
        status_code = response.status_code

        response.headers["X-Correlation-ID"] = correlation_id
        return response

    finally:
        duration = (time.perf_counter() - start_time) * 1000

        log_extra = {
            "correlation_id": correlation_id,
            "method": request.method,
            "url": str(request.url),
            "status_code": status_code,
            "duration_ms": round(duration, 2),
        }

        if status_code < 400:
            logger.info("request completed", extra=log_extra)
        elif status_code < 500:
            logger.warning("request completed", extra=log_extra)
        else:
            logger.error("request completed", extra=log_extra)
