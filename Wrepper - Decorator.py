def cursing_wrapper(func):
    def inner():
        print("Well,")
        func()
        print("You shithead")
    return inner


@cursing_wrapper
def say_hello():
    print("HELLO")

say_hello()



def counting_wrapper(func):
    def inner(name):
        for num in range (1,6):
            print(num)
        func(name)
        for num in range (6, 11):
            print(num)
    return inner

@counting_wrapper
def say_name(name:str):
    print(f"Hello, {name.capitalize()}")

say_name("amir")



def counting_wrapper(func):
    def inner(*args, **kwargs):
        for num in range(1, 6):
            print(num)
        func(*args, **kwargs)
        for num in range(6, 11):
            print(num)
    return inner



@counting_wrapper
def say_name(name: str):
    print(f"Hello, {name.capitalize()}")


say_name("amir")
