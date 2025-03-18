# 安全敏感决策动态推理PoC系统

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

基于动态属性感知和法规约束的AI安全决策验证系统，适配边缘计算环境。

## 功能特性
- 动态威胁指标与法律文本的联合编码
- 基于Deepseek-MoE的轻量化安全推理引擎
- 实时可视化决策轨迹追踪
- GDPR/ISO27001合规性自动检查

## 快速开始
```bash
# 安装依赖
pip install -r requirements.txt

# 启动可视化看板
streamlit run src/interface/dashboard.py

# 调用决策API
python -m uvicorn src.interface.api_server:app --reload
