def fibo(n:int) -> int:
    if n == 1 or n == 2:
        return n-1
    res = fibo(n-2) + fibo(n-1)
    return res

