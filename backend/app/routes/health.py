from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health", summary="Health Check")
async def health_check():
    """
    Returns service health status and confirmation that the Decision Arena API is operational.
    """
    return {
        "status": "ok",
        "message": "Decision Arena backend is running"
    }
