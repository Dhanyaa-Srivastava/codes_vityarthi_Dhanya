def zeta_approx(s, terms):
    """
    Approximate the Riemann zeta function ζ(s) by summing the first 'terms' terms of the series:
    ζ(s) = sum_{n=1}^∞ 1 / n^s for Re(s) > 1.
    
    Parameters:
    s (complex or float): The complex argument to the zeta function.
    terms (int): The number of terms to use in the approximation.
    
    Returns:
    float or complex: Approximate value of ζ(s).
    """
    total = 0
    for n in range(1, terms + 1):
        total += 1 / (n**s)
    return total

approx = zeta_approx(2, 1000)
print(f"Approximation of ζ(2) using 1000 terms: {approx}")
