# Testing Fibonacci number function
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def test_fibonacci():
    assert fib(0) == 0