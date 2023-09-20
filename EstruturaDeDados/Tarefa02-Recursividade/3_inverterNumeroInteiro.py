# 3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 – 321

def fibonacci_sequence(n: int) -> int:
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == "__main__":
    for i in range(1000):
        print(fibonacci_sequence(i))
