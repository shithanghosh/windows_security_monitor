from pydantic import BaseModel
from datetime import datetime

class ScanResult(BaseModel):
    scan_id: str
    timestamp: datetime
    status: str
