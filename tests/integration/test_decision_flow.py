def test_high_risk_scenario():
    test_case = {
        "network_indicators": {
            "threat_score": 0.92,
            "anomaly_types": ["SQLi", "XSS"],
            "traffic_pattern": {"src_ips": ["192.168.1.100"], "rate": 1500}
        },
        "legal_context": "GDPR-2023",
        "decision_context": "Database access request from external IP"
    }

    response = client.post("/decide", json=test_case)
    assert response.status_code == 200
    assert response.json()["decision"] == "BLOCK"
    assert "GDPR" in str(response.json()["reasoning_steps"])
