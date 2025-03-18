## 决策API端点

`POST /api/v1/decide`

**请求示例:**
```json
{
    "network_traffic": {
        "src_ip": "192.168.1.100",
        "dest_port": 443,
        "protocol": "HTTPS"
    },
    "legal_context": "GDPR-2024"
}
