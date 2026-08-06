def numbers():
    yield 10
    yield 20
    yield 50

gen = numbers()

for num in gen:
    print(num)