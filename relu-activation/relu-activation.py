import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    relu = np.asarray(x)
    return np.asarray(np.maximum(relu,0))