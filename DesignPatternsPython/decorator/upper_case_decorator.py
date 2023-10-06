def upper_case_decorator(fun):
    def wrapper(*args , **kargs):

        result = fun(*args , **kargs)

        return result.upper()
    return wrapper
    

@upper_case_decorator
def decorate(name):
    return f"Helo : {name}"

d = decorate(name="Akhlaq")

print(d)