from fastapi import APIRouter
router = APIRouter()

@router.get('/reports/latest')
def get_latest_report():
    return {'report_id': 'RPT-001', 'summary': 'No active threats detected.'}
