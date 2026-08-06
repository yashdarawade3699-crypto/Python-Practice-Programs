def opper():
    a=10
    b=56

    def combine():
         return a+b

    return combine

func = opper()
print(func())