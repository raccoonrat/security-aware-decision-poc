# API 参考文档
    
## 决策端点
    `POST /api/v1/decide`
    
    ### 请求格式
    ```json
    {
        "threat_indicators": {
            "severity": 0.85,
            "category": ["data_leakage", "unauthorized_access"]
        },
        "legal_context": "GDPR-2023"
    }

### 响应格式

    {
        "decision": "BLOCK",
        "confidence": 0.92,
        "compliance": ["GDPR Article 32"],
        "reasoning_chain": [
            {
                "step": 1,
                "action": "Threat Level Assessment",
                "result": "High Risk"
            }
        ]
    }
