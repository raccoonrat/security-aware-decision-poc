import torch
from transformers import AutoModel
from .threat_encoder import ThreatEncoder
from .law_encoder import LawGraphEncoder

class SafetyAwareMoE(nn.Module):
    def __init__(self, config):
        super().__init__()
        # 语言模型基座
        self.lm = AutoModel.from_pretrained(config.model_name)

        # 属性编码器
        self.threat_encoder = ThreatEncoder()
        self.law_encoder = LawGraphEncoder()

        # 动态路由
        self.gate_network = nn.Sequential(
            nn.Linear(self.lm.config.hidden_size, 64),
            nn.Tanh(),
            nn.Linear(64, 3)  # 3个专家
        )

        # 决策头
        self.decision_head = nn.Linear(
            self.lm.config.hidden_size + 64 + 32,  # 文本+威胁+法规
            2  # Allow/Block
        )

    def forward(self, text_input, threat_data, law_graph):
        # 文本特征提取
        text_features = self.lm(**text_input).last_hidden_state[:,0,:]

        # 属性编码
        threat_features = self.threat_encoder(threat_data)
        law_features = self.law_encoder(law_graph)

        # 门控融合
        gate_weights = torch.softmax(self.gate_network(text_features), dim=-1)
        fused_features = torch.cat([
            gate_weights[:,0:1] * text_features,
            gate_weights[:,1:2] * threat_features,
            gate_weights[:,2:3] * law_features
        ], dim=-1)

        # 决策输出
        logits = self.decision_head(fused_features)
        return logits
