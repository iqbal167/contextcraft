from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["infra"])


@router.get("/healthz")
def health():
    return {"status": "ok"}

