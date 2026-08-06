def add():
    a = 10
    b = 20

    def sum():
        return a + b

    return sum

func = add()
print(func())