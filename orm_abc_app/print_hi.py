import math

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def solution(a, b, c):
    if math.sqrt(a**2 + b**2) == c:
        result = " С является гипотенузой катетов A и B"
    else:
        result = "С не является гипотенузой катетов A и B"
    return result

if __name__ == '__main__':
    print_hi('PyCharm')
    result = solution(1, 2, 3)
    print(result)
