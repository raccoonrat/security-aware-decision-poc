import dgl
import torch
import torch.nn as nn

class LawGraphEncoder(nn.Module):
    def __init__(self, node_dim=128, out_dim=32):
        super().__init__()
        self.gcn_layers = nn.ModuleList([
            dgl.nn.GraphConv(node_dim, 64),
            dgl.nn.GraphConv(64, out_dim)
        ])

    def forward(self, g, node_features):
        h = node_features
        for i, conv in enumerate(self.gcn_layers):
            h = conv(g, h)
            if i != len(self.gcn_layers)-1:
                h = torch.relu(h)
        return h
