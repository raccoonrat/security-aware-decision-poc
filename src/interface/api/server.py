from fastapi import FastAPI
from src.core.decision_engine import DecisionEngine
from .schemas import DecisionRequest, DecisionResponse

app = FastAPI()
engine = DecisionEngine.load_from_config()

@app.post("/decide", response_model=DecisionResponse)
async def make_decision(request: DecisionRequest):
    threat_data = preprocess_threat(request.network_indicators)
    law_graph = build_law_graph(request.legal_context)

    decision_logits = engine(
        text=request.decision_context,
        threat_data=threat_data,
        law_graph=law_graph
    )

    return {
        "decision": "BLOCK" if decision_logits[1] > 0.7 else "ALLOW",
        "confidence": torch.sigmoid(decision_logits).tolist(),
        "reasoning_steps": engine.get_reasoning_path()
    }
