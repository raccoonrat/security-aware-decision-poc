import torch
import yaml

def load_pretrained(model_class, config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    model = model_class(**config)
    model.load_state_dict(torch.load(config['model_path']))
    return model

def export_onnx(model, sample_input, output_path):
    torch.onnx.export(
        model,
        sample_input,
        output_path,
        opset_version=13,
        input_names=['text', 'threat', 'law'],
        output_names=['decision']
    )
