from fastapi import APIRouter

router = APIRouter(tags=["infra"])


@router.get("/healthz")
def health():
    return {"status": "ok"}
