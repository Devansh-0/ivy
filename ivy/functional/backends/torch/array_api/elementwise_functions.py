import torch


def remainder(x1, x2: torch.Tensor) -> torch.Tensor:
    return torch.remainder(x1, x2)
