from ..models.model_utils import load_pretrained
from .threat_encoder import ThreatEncoder
from .law_encoder import LawGraphEncoder

class DecisionEngine:
    def __init__(self, config):
        self.threat_encoder = ThreatEncoder()
        self.law_encoder = LawGraphEncoder()
        self.model = load_pretrained(config)

    @classmethod
    def load_from_config(cls):
        with open("configs/model_config.yaml") as f:
            config = yaml.safe_load(f)
        return cls(config)

    def evaluate(self, input_data):
        threat_features = self.threat_encoder(input_data["threat"])
        law_features = self.law_encoder(input_data["law"])
        return self.model(threat_features, law_features)
