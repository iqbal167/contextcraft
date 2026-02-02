import logging
import sys

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s |  %(levelname)s | %(name)s | %(correlation_id)s | %(message)s | "
    "method=%(method)s | url=%(url)s | status=%(status_code)s | duration_ms=%(duration_ms)s"
)


def setup_logging(level: int = logging.INFO):
    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logging.getLogger("uvicorn.access").disabled = True

    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
