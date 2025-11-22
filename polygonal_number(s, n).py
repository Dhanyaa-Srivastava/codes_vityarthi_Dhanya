def polygonal_number(s, n):
    """
    Calculate the n-th s-gonal number.

    Parameters:
    s (int): Number of sides of the polygon (s >= 3).
    n (int): Term number (n >= 1).

    Returns:
    int: The n-th s-gonal number.
    """
    if s < 3 or n < 1:
        raise ValueError("Number of sides must be >= 3 and term number must be >= 1")

    return ((s - 2) * n * n - (s - 4) * n) // 2

x = int(input("Enter a number = "))
y = int(input("Enter a number = "))

print(polygonal_number(x, y))
# Example usage:
# polygonal_number(3, 4) gives the 4th triangular number = 10
# polygonal_number(4, 5) gives the 5th square number = 25
