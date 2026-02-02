import logging
import time

from fastapi import Request

# Logger for request middleware. contextcraft.request is used to log request details.
logger = logging.getLogger("contextcraft.request")

EXCLUDE_PATHS = {"/docs", "/openapi.json", "/api/v1/healthz"}


async def request_logging_middleware(request: Request, call_next):
    if request.url.path in EXCLUDE_PATHS:
        return await call_next(request)

    # Use perf_counter for high precision timing
    start_time = time.perf_counter()
    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response

    except Exception:
        logger.exception(
            "request failed with exception",
            extra={"method": request.method, "url": str(request.url)},
        )
        raise
    finally:
        duration = (time.perf_counter() - start_time) * 1000
        log_extra = {
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
