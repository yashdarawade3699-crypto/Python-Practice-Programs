def outer():
    message = "Hello from Closure!"

    def inner():
        print(message)

    return inner

# Create the closure
func = outer()

# Call the inner function
func()
