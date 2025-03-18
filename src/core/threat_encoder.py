import torch
import torch.nn as nn

class ThreatEncoder(nn.Module):
    def __init__(self, input_dim=5, hidden_dim=64):
        super().__init__()
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(input_dim, hidden_dim, kernel_size=3, padding=1),
            nn.LeakyReLU(),
            nn.MaxPool1d(2),
            nn.Dropout(0.2)
        )
        self.attention = nn.MultiheadAttention(hidden_dim, num_heads=4)

    def forward(self, x):
        # x shape: (batch_size, seq_len, features)
        x = x.permute(0, 2, 1)  # Conv1d expects (batch, features, seq)
        conv_out = self.temporal_conv(x)
        conv_out = conv_out.permute(2, 0, 1)  # (seq, batch, features)
        attn_out, _ = self.attention(conv_out, conv_out, conv_out)
        return attn_out.mean(dim=0)  # (batch, features)
