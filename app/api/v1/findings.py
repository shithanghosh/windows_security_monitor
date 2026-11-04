from fastapi import APIRouter
from app.models.finding import Finding
router = APIRouter()

@router.get('/findings', response_model=list[Finding])
def get_findings():
    return []
