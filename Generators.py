def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

for num in gen:
    print(num)