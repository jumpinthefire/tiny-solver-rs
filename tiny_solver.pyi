from typing import List, Tuple
import numpy as np
def mult(x: np.ndarray) -> np.ndarray: ...

class CostFactorSE2:
    def __init__(self, x: float, y: float, theta: float) -> None: ...

class Problem:
    def __init__(self) -> None: ...
    def add_residual_block(self, dim_residual: int, variable_key_size_list: List[Tuple[str, int]]) -> None: ...

class Factor:
    def __init__(self, a: ...) -> None: ...

class BetweenFactor:
    def __init__(self, x: np.ndarray, /) -> None: ...