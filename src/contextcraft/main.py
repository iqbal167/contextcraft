from fastapi import FastAPI

from contextcraft.api.v1 import api_router
from contextcraft.core.logging import setup_logging
from contextcraft.core.middleware import request_logging_middleware

setup_logging()

app = FastAPI()
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
