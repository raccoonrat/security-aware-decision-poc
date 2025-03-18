FROM nvcr.io/nvidia/pytorch:23.08-py3

WORKDIR /app
COPY . .

# 配置Jetson边缘设备支持
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "src/interface/dashboard.py"]
