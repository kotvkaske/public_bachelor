import torch
from torch import nn
class classic_lenet(nn.Module):
    def __init__(self):
        super(classic_lenet,self).__init__()
        self conv1 = nn.Conv2d(1,)