def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    W = 1.0 
    cumulative_returns = [] 

    for i in returns:
        W *=(1+i)
        cr = W - 1 
        cumulative_returns.append(cr)
    return cumulative_returns