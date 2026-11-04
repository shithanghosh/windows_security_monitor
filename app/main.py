from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api.v1 import health, scans, findings, recommendations, reports

setup_logging()

app = FastAPI(
    title="Windows Security Monitor API",
    description="Local Windows 10/11 Security Assessment Agent",
    version="0.2.0"
)

app.include_router(health.router, prefix='/api/v1', tags=["System"])
app.include_router(scans.router, prefix='/api/v1', tags=["Scans"])
app.include_router(findings.router, prefix='/api/v1', tags=["Findings"])
app.include_router(recommendations.router, prefix='/api/v1', tags=["Recommendations"])
app.include_router(reports.router, prefix='/api/v1', tags=["Reports"])
