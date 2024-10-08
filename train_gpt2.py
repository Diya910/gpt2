from dataclasses import dataclass
import torch
import torch.nn as nn
from torch.nn import functional as f

@datataclass
class GPTconfig:
    block_size: int 256
    vocab_size: int 65
    n_layer: int 6
    n_head: int 6
    n_embd: int 384 
    
class GPT(nn.Module):

    def __init__(self,config):
        super().__init__()
        self.config = config

        self.transformer = nn.ModuleDict(dict(
            wte = nn.Embedding(config.vocab_size, config.n_embd),
            wpe = nn.Embedding(config.block_size, config.n_embd),
            h = nn.ModuleList
        ))