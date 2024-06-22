'''
1. Viết class và cài phương thức softmax.
'''


import torch
import torch.nn as nn


class Softmax(nn.Module):
    """
    Softmax activation function module.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Compute the softmax activation function.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after applying softmax.
        """
        # Compute softmax
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x, dim=0, keepdim=True)
        return exp_x / sum_exp_x


class SoftmaxStable(nn.Module):
    """
    Stable Softmax activation function module.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        """
        Compute the stable softmax activation function.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after applying stable softmax.
        """
        # Compute stable softmax
        x_max = torch.max(x, dim=0, keepdim=True).values
        exp_x = torch.exp(x - x_max)
        sum_exp_x = torch.sum(exp_x, dim=0, keepdim=True)
        return exp_x / sum_exp_x
