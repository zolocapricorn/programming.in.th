def modulo():
    result = [(int(input()) % 42) for _ in range(10)]
    print(len(set(result)))
modulo()

