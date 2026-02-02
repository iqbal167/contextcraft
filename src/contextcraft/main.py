from fastapi import FastAPI, HTTPException

from contextcraft.api.v1 import api_router
from contextcraft.core.exception import (
    http_exception_handler,
    unhandled_exception_handler,
)
from contextcraft.core.logging import setup_logging
from contextcraft.core.middleware import request_logging_middleware

setup_logging()

app = FastAPI()
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.middleware("http")(request_logging_middleware)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "service": "contextcraft",
        "description": "RAG-powered learning notebook",
        "version": "0.1.0",
        "api": "/api/v1",
        "docs": "/docs",
    }
