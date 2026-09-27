import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    dot_prod = 0.0
    
    for i in range(len(x)):
        dot_prod += x[i]*y[i]
    return dot_prod