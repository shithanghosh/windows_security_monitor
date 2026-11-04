from pydantic import BaseModel

class Recommendation(BaseModel):
    check_id: str
    remediation_steps: list[str]
