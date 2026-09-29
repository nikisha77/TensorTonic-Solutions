import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    ans = 0
    for i in range(len(x)):
        ans += (x[i] - y[i]) ** 2
    return float(ans ** 0.5)   # square root, not * 0.5