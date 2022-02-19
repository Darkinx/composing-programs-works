def hello(func):
    def inner():
        print("Hello ")
        func() 
    return inner


# @hello
def name():
    print("Alice")

# if __name__ == "__main__":
#     name()

obj = hello(name)
obj()


# see : https://pythonbasics.org/decorators/