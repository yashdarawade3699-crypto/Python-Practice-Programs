def add():
    a = 10
    b = 45

    def sum():
        return a + b

    return sum

func = add()
print(func())