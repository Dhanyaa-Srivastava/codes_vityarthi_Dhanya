**Number Theory Function Library – Python
Overview of the Project**

This project is a complete collection of number-theory-based Python functions implemented as part of a Practical Lab Manual.
It includes 40+ mathematical utility functions such as Euler’s Totient Function, Möbius Function, Prime Factorization, Digital Root, Modular Arithmetic, and more.
The goal is to help students understand the logic behind mathematical algorithms while providing efficient, clean, and reusable Python implementations.
These programs demonstrate core algorithmic skills such as factorization, recursion, modular arithmetic, sieve methods, trial division, and time-efficient computation.

**Features**

- ✔️ 40+ number-theory functions
- ✔️ Each program includes aim, methodology, description, code, and output
- ✔️ Covers divisor functions, prime functions, digit analysis, modular arithmetic, sequence generation, and special number checks
- ✔️ Optimized algorithms using √n logic, sieves, and efficient arithmetic
- ✔️ Clean, modular, reusable code structure
- ✔️ Suitable for academic lab manuals, assignments, and competitive programming
- ✔️ User-friendly and beginner-friendly Python scripts

**Technologies / Tools Used**

**Programming Language: Python 3
Tools & Libraries:**
- math module for mathematical operations
- time module for execution analysis
- Python built-ins like pow(), list comprehensions, loops, and conditionals

**Algorithms Used:**
- Trial division
- Sieve of Eratosthenes
- Square-root divisor detection
- Modular exponentiation
- Recursion and iterative loops

**Steps to Install & Run the Project**
1. Clone this Repository

- git clone https://github.com/your-username/number-theory-lab.git
  cd number-theory-lab

2. Install Python (if not already installed)

Download from: https://python.org
Check version:
- python --version

3. Run Any Program

Each function is saved as a separate .py file (e.g., euler_phi.py, mobius.py).
To run:

- python euler_phi.py
Or:
- python practical_01_euler_phi.py

4. Run All Programs (if combined into one file)
- python main.py

**Instructions for Testing**
1. Manual Testing

- Run each function file individually.
- Provide sample inputs as shown in your lab manual (e.g., 10, 36, 122)
- Compare output with expected values inside the PDF/lab notes.

2. Use Automated Test Scripts (Optional)

If you create a test script:
- python test_functions.py

3. Edge Case Testing

Test special inputs:

- 0 
- 1
- Negative numbers
- Prime numbers
- Large inputs (for performance testing)

4. Mathematical Verification

Use known results to verify correctness:

- φ(10) = 4
- μ(36) = 0
- prime_factors(16) = [2,2,2,2]
- digital_root(122) = 5
