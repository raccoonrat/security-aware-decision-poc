import torch
from models.model_utils import export_onnx

def main():
    model = torch.load("models/safety_model.pt")
    sample_input = (
        torch.randn(1, 128),   # text
        torch.randn(1, 5),     # threat
        torch.randn(1, 10, 32) # law
    )
    export_onnx(model, sample_input, "models/jetson_model.onnx")

if __name__ == "__main__":
    main()
