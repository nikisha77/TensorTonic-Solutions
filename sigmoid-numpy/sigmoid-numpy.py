import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:

    l = np.asarray(x,dtype=float)

    if l.ndim ==0:
        return 1/(1+np.exp(-l))

    a = []

    for i in l:
        s = 1/(1+np.exp(-i))
        a.append(s)

    return np.asarray(a)