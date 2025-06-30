from fastapi import APIRouter

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("")
async def analyze_data():
    """Analyze uploaded data (placeholder)."""
    return {"result": "analysis"}
