from pydantic import BaseModel

class NetworkIndicators(BaseModel):
    threat_score: float
    anomaly_types: list[str]
    traffic_pattern: dict

class DecisionRequest(BaseModel):
    network_indicators: NetworkIndicators
    legal_context: str
    decision_context: str

class DecisionResponse(BaseModel):
    decision: str
    confidence: list[float]
    reasoning_steps: list[dict]
