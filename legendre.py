def p(a, p):
    # Calculate a^((p-1)//2) mod p
    result = pow(a, (p - 1) // 2, p)
    if result == p - 1:
        return -1
    else:
        return result

# Example usage:
a = 3
p_val = 7  # an odd prime

legendre_symbol = p(a, p_val)
print(f"The Legendre symbol ({a}/{p_val}) is {legendre_symbol}")
