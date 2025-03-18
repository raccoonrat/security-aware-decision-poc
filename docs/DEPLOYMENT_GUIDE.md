```markdown
# 部署指南

## 边缘设备部署
```bash
# 转换ONNX模型
python scripts/convert_to_jetson.py --input models/safety_model.pt

# 启动边缘服务
docker run -p 8501:8501 security-poc --platform jetson

# 云原生部署

    # 创建Kubernetes集群
    helm install security-poc charts/ \
        --set replicaCount=3 \
        --set modelStorage.s3Bucket=my-models
