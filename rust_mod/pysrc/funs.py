
def sum_loop(number: int) -> int:
    sum = 0
    moda = 100
    modb = 99
    for i in range(number):
        sum = (sum + i % moda) % modb
    return sum

def get_fibonacci(number: int) -> int:
    """Get the nth Fibonacci number."""
    if number == 1:
        return 1
    elif number == 2:
        return 2

    total = 0
    last = 0
    current = 1
    for _ in range(1, number):
        total = last + current
        last = current
        current = total
    return total
