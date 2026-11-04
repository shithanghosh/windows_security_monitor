from pydantic import BaseModel

class RecommendationAction(BaseModel):
    action: str
    requires_approval: bool
    automatic_remediation: bool

class Finding(BaseModel):
    finding_id: str
    check_id: str
    title: str
    severity: str
    confidence: str
    status: str
    recommendation: RecommendationAction
