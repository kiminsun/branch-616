def fibo(i):
    if i < 2:
        return i
    else:
        return fibo(i-1) + fibo(i-2)

if __name__ == '__main':
    print(fibo(1))
    print(fibo(2))
    print(fibo(3))
    print(fibo(4))
